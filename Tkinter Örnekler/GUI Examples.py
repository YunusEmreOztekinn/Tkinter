import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

data1 = { 'Yıllar':['2002','2003','2004','2005','2006','2007','2008','2009'],
          'GSYH':[238,312,405,501,552,676,764,645]
}
df1 = DataFrame(data1,columns=['Yıllar','GSYH'])


data2 = { 'Yıllar': ['1930','1940','1950','1960','1970','1980','1990','2000','2010'],
          'İşsizlik_Yüzdesi': [12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
}

df2 = DataFrame(data2, columns=['Yıllar','İşsizlik_Yüzdesi'])


data3 = {'Aylar': ['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık'],
         'Sıcaklık_Ortalaması':[0.1,1.6,5.7,11.2,16.0,19.9,23.3,23.3,18.8,13.1,7.2,2.4]

         }

df3 = DataFrame(data3, columns=['Aylar','Sıcaklık_Ortalaması'])

root = tk.Tk()
figure1 = plt.Figure(figsize=(5,5),dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1,root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df1 = df1[['Yıllar','GSYH']].groupby('Yıllar').sum()
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Yillar x GSYH')

figure2 = plt.Figure(figsize=(5,5),dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2,root)
line2.get_tk_widget().pack(side=tk.LEFT,fill=tk.BOTH)
df2 = df2[['Yıllar','İşsizlik_Yüzdesi']].groupby('Yıllar').sum()
df2.plot(kind='line',legend=True,ax=ax2, color='r',marker='o',fontsize=10)
ax2.set_title('Yıllar x İşsizlik Yüzdesi')

figure3 = plt.Figure(figsize=(9,5),dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df3['Aylar'], df3['Sıcaklık_Ortalaması'], color='g')
scatter3 = FigureCanvasTkAgg(figure3,root)
scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax3.legend(['Sıcaklık_Ortalaması'])
ax3.set_xlabel('Aylar')
ax3.set_title('Aylar x Sıcaklık Ortalaması')

root.mainloop()