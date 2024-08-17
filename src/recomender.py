from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_distances

from mlxtend.frequent_patterns import apriori, association_rules



# Class Recomendasi System Content base
class RecommenderSystem:
    def __init__(self, df, series1, series2):
        self.df_bank_stock = df.loc[:, [series1, series2]]
        self.df_bank_stock.drop_duplicates(subset='StockCode', keep='first', inplace=True)
        self.df = self.df_bank_stock.loc[:, [series1, series2]]
        self.series1 = series1
        self.series2 = series2
        self.encoder = None
        self.bank = None
        
    def fit(self):
        self.encoder = CountVectorizer(stop_words="english", tokenizer=word_tokenize)
        self.bank = self.encoder.fit_transform(self.df[self.series2])
        
    def recommend(self, stockcode, topk=10):
        # Memastikan stockcode ada di DataFrame
        if stockcode not in self.df[self.series1].values:
            raise ValueError("Stockcode tidak ditemukan dalam dataset")
        
        # Mengambil deskripsi berdasarkan stockcode
        description = self.df[self.df[self.series1] == stockcode][self.series2].values[0]
        code = self.encoder.transform([description])
        
        # Menghitung jarak cosine dan mencari item yang paling mirip
        dist = cosine_distances(code, self.bank)
        rec_indices = dist.argsort()[0, 1:(topk+1)]
        return self.df.iloc[rec_indices]
    

# Class Recomender Basket Produk
class RecomendBasketProduk:
    def __init__(self, df, country, column_country, column_invoice, column_desc, column_qty):
        self.df = df
        self.country = country
        self.column_country = column_country
        self.column_invoice = column_invoice
        self.column_desc = column_desc
        self.column_qty = column_qty
        self.basket_df = None
        self.basket_onehot = None
        self.frequent_itemsets = None
        self.rules = None
    
    def transform_one_hot(self):
        # Filter data based on selected country
        self.basket_df = self.df[self.df[self.column_country] == self.country]
        # Group by invoice and description, then sum the quantity
        self.basket_onehot = (self.basket_df
                              .groupby([self.column_invoice, self.column_desc])[self.column_qty]
                              .sum()
                              .unstack()
                              .reset_index()
                              .fillna(0)
                              .set_index(self.column_invoice))
        # Convert the data to one-hot encoding
        self.basket_onehot = self.basket_onehot.applymap(lambda x: 1 if x > 0 else 0)
        
    def fit(self, min_support=0.1):
        # Ensure one-hot transformation is applied
        if self.basket_onehot is None:
            self.transform_one_hot()
        # Apply the apriori algorithm to find frequent itemsets
        self.frequent_itemsets = apriori(self.basket_onehot, min_support=min_support, use_colnames=True)
        # Generate association rules from the frequent itemsets
        self.rules = association_rules(self.frequent_itemsets, metric='lift', min_threshold=1)
    
    def recommend(self, topk=10):
        # Sort rules by confidence and lift, then get the top k
        sorted_rules = self.rules.sort_values(['confidence', 'lift'], ascending=[False, False]).head(topk).reset_index(drop=True)
        # Format antecedents and consequents as strings
        sorted_rules['antecedents'] = sorted_rules['antecedents'].apply(lambda x: ', '.join(list(x)))
        sorted_rules['consequents'] = sorted_rules['consequents'].apply(lambda x: ', '.join(list(x)))
        return sorted_rules[['antecedents', 'consequents', 'confidence', 'lift']]

    
