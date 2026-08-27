#%%



# Publikfavoriterna når nästan maximalt betyg

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/movies.csv")

# Ta fram top 10 filmer
top10 = df.sort_values("vote_average", ascending=False).head(10).sort_values("vote_average")

colors = ['gray'] * 9 + ['red']

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.barh(top10["title"], top10["vote_average"], color=colors)

# Visa betyg på varje bar
for bar in bars:
    val = bar.get_width()
    ax.text(val + 0.05, bar.get_y() + 0.3, f'{val:.2f}', va='center', fontsize=9)

# Annotation (Storytelling)
best_rating = top10.iloc[-1]["vote_average"]
ax.annotate(f'Högst betyg: {best_rating:.2f}', 
            xy=(best_rating, 9), 
            xytext=(best_rating - 2.5, 7.5),
            arrowprops=dict(arrowstyle='->', color='red'),
            color='red', fontsize=10, fontweight='bold')

# Titel och layout
ax.set_title('Publikfavoriterna når nästan maximalt betyg', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Genomsnittligt betyg')
ax.set_xlim(0, 10)

# Rensa grafformat (Decluttering)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='x', alpha=0.3, linestyle='--')


plt.tight_layout()
plt.show()
# %%
