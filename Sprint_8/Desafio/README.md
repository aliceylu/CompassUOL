# DESAFIO - PROPOSTA

## Tema: Ação/Aventura

Para o desafio proposto, serão utilizados as duas principais franquias de filmes do ator Keanu Reeves, sendo elas Matrix e John Wick. Cada um dos 8 filmes será analisado individualmente. 
Primeiramente, será realizado um comparativo com os 5 filmes de ação e aventura mais famosos lançados nos anos correspondentes aos da base. Serão comparados os quesitos: orçamento versus bilheteria.
Em um segundo momento, os dados recebidos serão analisados em busca de um padrão de atores/atrizes nos filmes que fizeram sucesso.
E por fim, será analisado a popularidade do ator Keanu Reeves com o passar dos anos, analisando a bilheteria de todos os seus filmes e a participação do mesmo em filmes onde ele não era o ator principal.

------------------------------------------------
Endpoints utilizados:

https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&primary_release_year=2023&sort_by=popularity.desc&with_genres=12%2C28

https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&primary_release_year=2021&sort_by=popularity.desc&with_genres=12%2C28

https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&primary_release_year=2019&sort_by=popularity.desc&with_genres=12%2C28

https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&primary_release_year=2017&sort_by=popularity.desc&with_genres=12%2C28

https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&primary_release_year=2015&sort_by=popularity.desc&with_genres=12%2C28

https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&primary_release_year=2003&sort_by=popularity.desc&with_genres=12%2C28

https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&primary_release_year=1999&sort_by=popularity.desc&with_genres=12%2C28



TMDB_ID = ['640146', '447365', '620705', '420808', '948713', '455476', '385128', '634649', '566525', '580489', '460465', '791373', '384018', '299534', '429617', '299537', '181812', '447404', '283995', '335988', '315635', '284053', '47971', '166426', '99861', '87101', '76341', '135397', '102899', '140607', '22', '122', '604', '605', '1927', '9471', '14411', '8961', '9486', '6038', '564', '1893', '1911', '36643', '10047', '8487', '624860', '604', '605', '603', '245891', '324552', '458156', '603692', '168259', '216015', '303857', '99861', '312221', '150540']

OMDB_ID = ["tt2911666", "tt4425200", "tt6146586", "tt10366206", "tt0133093", "tt0234215", "tt0242653", "tt10838180"]

NYT_URL = "https://api.nytimes.com/svc/movies/v2/reviews/search.json?query=Keanu%20Reeves&api-key={}"
