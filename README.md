# Banco de dados Solo Criado

 Este é um programa para coletar e organizar dados de estoques de Solo Criado do município de Porto Alegre

## Roadmap

* Coletar listagem do site da prefeitura
* Transformar pdf da listagem em xmls por este site
* Transformar xmls em cvs
* Carregar cvs de listagem para o banco de dados
  * Extração;
  * Exploração;
  * Limpeza;
  * Agregação;
  * Visualização;
  * Storytelling.

## Links

Links uteis para a consulta durante o projeto:

* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Pandas](https://pandas.pydata.org/pandas-docs/stable/pandas.pdf)
* [Seaborn](https://seaborn.pydata.org/#)
* [Selenium](https://selenium-python.readthedocs.io/)
* [Scrapy](https://docs.scrapy.org/en/latest/)
* [Requests](https://docs.python-requests.org/en/latest/)
* [pyQGIS](https://docs.qgis.org/3.22/pt_BR/docs/pyqgis_developer_cookbook/index.html)
* [Geopandas](https://geopandas.org/en/stable/docs.html)

* [Listagens de Estoque de Solo Criado](http://www2.portoalegre.rs.gov.br/edificapoa/default.php?p_secao=1445)
* [ilovepdf](https://www.ilovepdf.com/pt)

## Primeiros passos

Na primeira versão do programa vou considerar que eu já baixei os pdfs do site da prefeitura e converti eles para excel usando a ferramenta do ilovepdf. Posteriormente vou tentar automatizar o processo de modo que o programa baixe automaticamente o pdf e o converta via web. Portanto, primeiramente vou focar na limpeza e agregação dos dados.
