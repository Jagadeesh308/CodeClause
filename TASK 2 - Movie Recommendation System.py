{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "113e0b03",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "id": "7010363b",
   "metadata": {},
   "outputs": [],
   "source": [
    "movies=pd.read_csv(\"movie.csv\")\n",
    "credits=pd.read_csv(\"movie_credit.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "8418791a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>budget</th>\n",
       "      <th>genres</th>\n",
       "      <th>homepage</th>\n",
       "      <th>id</th>\n",
       "      <th>keywords</th>\n",
       "      <th>original_language</th>\n",
       "      <th>original_title</th>\n",
       "      <th>overview</th>\n",
       "      <th>popularity</th>\n",
       "      <th>production_companies</th>\n",
       "      <th>production_countries</th>\n",
       "      <th>release_date</th>\n",
       "      <th>revenue</th>\n",
       "      <th>runtime</th>\n",
       "      <th>spoken_languages</th>\n",
       "      <th>status</th>\n",
       "      <th>tagline</th>\n",
       "      <th>title</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>vote_count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>237000000</td>\n",
       "      <td>[{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...</td>\n",
       "      <td>http://www.avatarmovie.com/</td>\n",
       "      <td>19995</td>\n",
       "      <td>[{\"id\": 1463, \"name\": \"culture clash\"}, {\"id\":...</td>\n",
       "      <td>en</td>\n",
       "      <td>Avatar</td>\n",
       "      <td>In the 22nd century, a paraplegic Marine is di...</td>\n",
       "      <td>150.437577</td>\n",
       "      <td>[{\"name\": \"Ingenious Film Partners\", \"id\": 289...</td>\n",
       "      <td>[{\"iso_3166_1\": \"US\", \"name\": \"United States o...</td>\n",
       "      <td>2009-12-10</td>\n",
       "      <td>2787965087</td>\n",
       "      <td>162.0</td>\n",
       "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}, {\"iso...</td>\n",
       "      <td>Released</td>\n",
       "      <td>Enter the World of Pandora.</td>\n",
       "      <td>Avatar</td>\n",
       "      <td>7.2</td>\n",
       "      <td>11800</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>300000000</td>\n",
       "      <td>[{\"id\": 12, \"name\": \"Adventure\"}, {\"id\": 14, \"...</td>\n",
       "      <td>http://disney.go.com/disneypictures/pirates/</td>\n",
       "      <td>285</td>\n",
       "      <td>[{\"id\": 270, \"name\": \"ocean\"}, {\"id\": 726, \"na...</td>\n",
       "      <td>en</td>\n",
       "      <td>Pirates of the Caribbean: At World's End</td>\n",
       "      <td>Captain Barbossa, long believed to be dead, ha...</td>\n",
       "      <td>139.082615</td>\n",
       "      <td>[{\"name\": \"Walt Disney Pictures\", \"id\": 2}, {\"...</td>\n",
       "      <td>[{\"iso_3166_1\": \"US\", \"name\": \"United States o...</td>\n",
       "      <td>2007-05-19</td>\n",
       "      <td>961000000</td>\n",
       "      <td>169.0</td>\n",
       "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}]</td>\n",
       "      <td>Released</td>\n",
       "      <td>At the end of the world, the adventure begins.</td>\n",
       "      <td>Pirates of the Caribbean: At World's End</td>\n",
       "      <td>6.9</td>\n",
       "      <td>4500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>245000000</td>\n",
       "      <td>[{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...</td>\n",
       "      <td>http://www.sonypictures.com/movies/spectre/</td>\n",
       "      <td>206647</td>\n",
       "      <td>[{\"id\": 470, \"name\": \"spy\"}, {\"id\": 818, \"name...</td>\n",
       "      <td>en</td>\n",
       "      <td>Spectre</td>\n",
       "      <td>A cryptic message from Bond’s past sends him o...</td>\n",
       "      <td>107.376788</td>\n",
       "      <td>[{\"name\": \"Columbia Pictures\", \"id\": 5}, {\"nam...</td>\n",
       "      <td>[{\"iso_3166_1\": \"GB\", \"name\": \"United Kingdom\"...</td>\n",
       "      <td>2015-10-26</td>\n",
       "      <td>880674609</td>\n",
       "      <td>148.0</td>\n",
       "      <td>[{\"iso_639_1\": \"fr\", \"name\": \"Fran\\u00e7ais\"},...</td>\n",
       "      <td>Released</td>\n",
       "      <td>A Plan No One Escapes</td>\n",
       "      <td>Spectre</td>\n",
       "      <td>6.3</td>\n",
       "      <td>4466</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      budget                                             genres  \\\n",
       "0  237000000  [{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...   \n",
       "1  300000000  [{\"id\": 12, \"name\": \"Adventure\"}, {\"id\": 14, \"...   \n",
       "2  245000000  [{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...   \n",
       "\n",
       "                                       homepage      id  \\\n",
       "0                   http://www.avatarmovie.com/   19995   \n",
       "1  http://disney.go.com/disneypictures/pirates/     285   \n",
       "2   http://www.sonypictures.com/movies/spectre/  206647   \n",
       "\n",
       "                                            keywords original_language  \\\n",
       "0  [{\"id\": 1463, \"name\": \"culture clash\"}, {\"id\":...                en   \n",
       "1  [{\"id\": 270, \"name\": \"ocean\"}, {\"id\": 726, \"na...                en   \n",
       "2  [{\"id\": 470, \"name\": \"spy\"}, {\"id\": 818, \"name...                en   \n",
       "\n",
       "                             original_title  \\\n",
       "0                                    Avatar   \n",
       "1  Pirates of the Caribbean: At World's End   \n",
       "2                                   Spectre   \n",
       "\n",
       "                                            overview  popularity  \\\n",
       "0  In the 22nd century, a paraplegic Marine is di...  150.437577   \n",
       "1  Captain Barbossa, long believed to be dead, ha...  139.082615   \n",
       "2  A cryptic message from Bond’s past sends him o...  107.376788   \n",
       "\n",
       "                                production_companies  \\\n",
       "0  [{\"name\": \"Ingenious Film Partners\", \"id\": 289...   \n",
       "1  [{\"name\": \"Walt Disney Pictures\", \"id\": 2}, {\"...   \n",
       "2  [{\"name\": \"Columbia Pictures\", \"id\": 5}, {\"nam...   \n",
       "\n",
       "                                production_countries release_date     revenue  \\\n",
       "0  [{\"iso_3166_1\": \"US\", \"name\": \"United States o...   2009-12-10  2787965087   \n",
       "1  [{\"iso_3166_1\": \"US\", \"name\": \"United States o...   2007-05-19   961000000   \n",
       "2  [{\"iso_3166_1\": \"GB\", \"name\": \"United Kingdom\"...   2015-10-26   880674609   \n",
       "\n",
       "   runtime                                   spoken_languages    status  \\\n",
       "0    162.0  [{\"iso_639_1\": \"en\", \"name\": \"English\"}, {\"iso...  Released   \n",
       "1    169.0           [{\"iso_639_1\": \"en\", \"name\": \"English\"}]  Released   \n",
       "2    148.0  [{\"iso_639_1\": \"fr\", \"name\": \"Fran\\u00e7ais\"},...  Released   \n",
       "\n",
       "                                          tagline  \\\n",
       "0                     Enter the World of Pandora.   \n",
       "1  At the end of the world, the adventure begins.   \n",
       "2                           A Plan No One Escapes   \n",
       "\n",
       "                                      title  vote_average  vote_count  \n",
       "0                                    Avatar           7.2       11800  \n",
       "1  Pirates of the Caribbean: At World's End           6.9        4500  \n",
       "2                                   Spectre           6.3        4466  "
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "id": "4154d42f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4803, 20)"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "3b8d440c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>movie_id</th>\n",
       "      <th>title</th>\n",
       "      <th>cast</th>\n",
       "      <th>crew</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>19995</td>\n",
       "      <td>Avatar</td>\n",
       "      <td>[{\"cast_id\": 242, \"character\": \"Jake Sully\", \"...</td>\n",
       "      <td>[{\"credit_id\": \"52fe48009251416c750aca23\", \"de...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>285</td>\n",
       "      <td>Pirates of the Caribbean: At World's End</td>\n",
       "      <td>[{\"cast_id\": 4, \"character\": \"Captain Jack Spa...</td>\n",
       "      <td>[{\"credit_id\": \"52fe4232c3a36847f800b579\", \"de...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>206647</td>\n",
       "      <td>Spectre</td>\n",
       "      <td>[{\"cast_id\": 1, \"character\": \"James Bond\", \"cr...</td>\n",
       "      <td>[{\"credit_id\": \"54805967c3a36829b5002c41\", \"de...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>49026</td>\n",
       "      <td>The Dark Knight Rises</td>\n",
       "      <td>[{\"cast_id\": 2, \"character\": \"Bruce Wayne / Ba...</td>\n",
       "      <td>[{\"credit_id\": \"52fe4781c3a36847f81398c3\", \"de...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>49529</td>\n",
       "      <td>John Carter</td>\n",
       "      <td>[{\"cast_id\": 5, \"character\": \"John Carter\", \"c...</td>\n",
       "      <td>[{\"credit_id\": \"52fe479ac3a36847f813eaa3\", \"de...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   movie_id                                     title  \\\n",
       "0     19995                                    Avatar   \n",
       "1       285  Pirates of the Caribbean: At World's End   \n",
       "2    206647                                   Spectre   \n",
       "3     49026                     The Dark Knight Rises   \n",
       "4     49529                               John Carter   \n",
       "\n",
       "                                                cast  \\\n",
       "0  [{\"cast_id\": 242, \"character\": \"Jake Sully\", \"...   \n",
       "1  [{\"cast_id\": 4, \"character\": \"Captain Jack Spa...   \n",
       "2  [{\"cast_id\": 1, \"character\": \"James Bond\", \"cr...   \n",
       "3  [{\"cast_id\": 2, \"character\": \"Bruce Wayne / Ba...   \n",
       "4  [{\"cast_id\": 5, \"character\": \"John Carter\", \"c...   \n",
       "\n",
       "                                                crew  \n",
       "0  [{\"credit_id\": \"52fe48009251416c750aca23\", \"de...  \n",
       "1  [{\"credit_id\": \"52fe4232c3a36847f800b579\", \"de...  \n",
       "2  [{\"credit_id\": \"54805967c3a36829b5002c41\", \"de...  \n",
       "3  [{\"credit_id\": \"52fe4781c3a36847f81398c3\", \"de...  \n",
       "4  [{\"credit_id\": \"52fe479ac3a36847f813eaa3\", \"de...  "
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "credits.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "id": "349d9bde",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'[{\"id\": 1463, \"name\": \"culture clash\"}, {\"id\": 2964, \"name\": \"future\"}, {\"id\": 3386, \"name\": \"space war\"}, {\"id\": 3388, \"name\": \"space colony\"}, {\"id\": 3679, \"name\": \"society\"}, {\"id\": 3801, \"name\": \"space travel\"}, {\"id\": 9685, \"name\": \"futuristic\"}, {\"id\": 9840, \"name\": \"romance\"}, {\"id\": 9882, \"name\": \"space\"}, {\"id\": 9951, \"name\": \"alien\"}, {\"id\": 10148, \"name\": \"tribe\"}, {\"id\": 10158, \"name\": \"alien planet\"}, {\"id\": 10987, \"name\": \"cgi\"}, {\"id\": 11399, \"name\": \"marine\"}, {\"id\": 13065, \"name\": \"soldier\"}, {\"id\": 14643, \"name\": \"battle\"}, {\"id\": 14720, \"name\": \"love affair\"}, {\"id\": 165431, \"name\": \"anti war\"}, {\"id\": 193554, \"name\": \"power relations\"}, {\"id\": 206690, \"name\": \"mind and soul\"}, {\"id\": 209714, \"name\": \"3d\"}]'"
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies[\"keywords\"][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "984f0ef9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Enter the World of Pandora.'"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies[\"tagline\"][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "id": "4015f6f7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'In the 22nd century, a paraplegic Marine is dispatched to the moon Pandora on a unique mission, but becomes torn between following orders and protecting an alien civilization.'"
      ]
     },
     "execution_count": 136,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies[\"overview\"][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "id": "a5b14a1c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       [{\"cast_id\": 242, \"character\": \"Jake Sully\", \"...\n",
       "1       [{\"cast_id\": 4, \"character\": \"Captain Jack Spa...\n",
       "2       [{\"cast_id\": 1, \"character\": \"James Bond\", \"cr...\n",
       "3       [{\"cast_id\": 2, \"character\": \"Bruce Wayne / Ba...\n",
       "4       [{\"cast_id\": 5, \"character\": \"John Carter\", \"c...\n",
       "                              ...                        \n",
       "4798    [{\"cast_id\": 1, \"character\": \"El Mariachi\", \"c...\n",
       "4799    [{\"cast_id\": 1, \"character\": \"Buzzy\", \"credit_...\n",
       "4800    [{\"cast_id\": 8, \"character\": \"Oliver O\\u2019To...\n",
       "4801    [{\"cast_id\": 3, \"character\": \"Sam\", \"credit_id...\n",
       "4802    [{\"cast_id\": 3, \"character\": \"Herself\", \"credi...\n",
       "Name: cast, Length: 4803, dtype: object"
      ]
     },
     "execution_count": 137,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "credits[\"cast\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "id": "15e1ca74",
   "metadata": {},
   "outputs": [],
   "source": [
    "movies=movies.merge(credits,on=\"title\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "id": "bec65931",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 4809 entries, 0 to 4808\n",
      "Data columns (total 23 columns):\n",
      " #   Column                Non-Null Count  Dtype  \n",
      "---  ------                --------------  -----  \n",
      " 0   budget                4809 non-null   int64  \n",
      " 1   genres                4809 non-null   object \n",
      " 2   homepage              1713 non-null   object \n",
      " 3   id                    4809 non-null   int64  \n",
      " 4   keywords              4809 non-null   object \n",
      " 5   original_language     4809 non-null   object \n",
      " 6   original_title        4809 non-null   object \n",
      " 7   overview              4806 non-null   object \n",
      " 8   popularity            4809 non-null   float64\n",
      " 9   production_companies  4809 non-null   object \n",
      " 10  production_countries  4809 non-null   object \n",
      " 11  release_date          4808 non-null   object \n",
      " 12  revenue               4809 non-null   int64  \n",
      " 13  runtime               4807 non-null   float64\n",
      " 14  spoken_languages      4809 non-null   object \n",
      " 15  status                4809 non-null   object \n",
      " 16  tagline               3965 non-null   object \n",
      " 17  title                 4809 non-null   object \n",
      " 18  vote_average          4809 non-null   float64\n",
      " 19  vote_count            4809 non-null   int64  \n",
      " 20  movie_id              4809 non-null   int64  \n",
      " 21  cast                  4809 non-null   object \n",
      " 22  crew                  4809 non-null   object \n",
      "dtypes: float64(3), int64(5), object(15)\n",
      "memory usage: 901.7+ KB\n"
     ]
    }
   ],
   "source": [
    "movies.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "id": "fe8ba4d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import ast"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "id": "cd3f8e18",
   "metadata": {},
   "outputs": [],
   "source": [
    "def str_list(a):\n",
    "  a=ast.literal_eval(a)\n",
    "  m=[]\n",
    "  for item in a:\n",
    "    m.append(item['name'])\n",
    "  return m"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "id": "8158e964",
   "metadata": {},
   "outputs": [],
   "source": [
    "movies[\"cast\"]=movies[\"cast\"].apply(str_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "id": "40a39bfd",
   "metadata": {},
   "outputs": [],
   "source": [
    "def str2_list(a):\n",
    "  a=ast.literal_eval(a)\n",
    "  m=[]\n",
    "  for item in a:\n",
    "    if item['job']==\"Director\":\n",
    "      m.append(item['name'])\n",
    "  return m"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "id": "8f8a9455",
   "metadata": {},
   "outputs": [],
   "source": [
    "movies[\"crew\"]=movies[\"crew\"].apply(str2_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "id": "ac37f2c8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       [Sam Worthington, Zoe Saldana, Sigourney Weave...\n",
       "1       [Johnny Depp, Orlando Bloom, Keira Knightley, ...\n",
       "2       [Daniel Craig, Christoph Waltz, Léa Seydoux, R...\n",
       "3       [Christian Bale, Michael Caine, Gary Oldman, A...\n",
       "4       [Taylor Kitsch, Lynn Collins, Samantha Morton,...\n",
       "                              ...                        \n",
       "4804    [Carlos Gallardo, Jaime de Hoyos, Peter Marqua...\n",
       "4805    [Edward Burns, Kerry Bishé, Marsha Dietlein, C...\n",
       "4806    [Eric Mabius, Kristin Booth, Crystal Lowe, Geo...\n",
       "4807    [Daniel Henney, Eliza Coupe, Bill Paxton, Alan...\n",
       "4808    [Drew Barrymore, Brian Herzlinger, Corey Feldm...\n",
       "Name: cast, Length: 4809, dtype: object"
      ]
     },
     "execution_count": 145,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies[\"cast\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "id": "ffc898a3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0                                [James Cameron]\n",
       "1                               [Gore Verbinski]\n",
       "2                                   [Sam Mendes]\n",
       "3                            [Christopher Nolan]\n",
       "4                               [Andrew Stanton]\n",
       "                          ...                   \n",
       "4804                          [Robert Rodriguez]\n",
       "4805                              [Edward Burns]\n",
       "4806                               [Scott Smith]\n",
       "4807                               [Daniel Hsia]\n",
       "4808    [Brian Herzlinger, Jon Gunn, Brett Winn]\n",
       "Name: crew, Length: 4809, dtype: object"
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies[\"crew\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "id": "1b5a531f",
   "metadata": {},
   "outputs": [],
   "source": [
    "movies[\"genres\"]=movies['genres'].apply(str_list)\n",
    "movies[\"keywords\"]=movies['keywords'].apply(str_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "id": "816a1f05",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "budget                     0\n",
       "genres                     0\n",
       "homepage                3096\n",
       "id                         0\n",
       "keywords                   0\n",
       "original_language          0\n",
       "original_title             0\n",
       "overview                   3\n",
       "popularity                 0\n",
       "production_companies       0\n",
       "production_countries       0\n",
       "release_date               1\n",
       "revenue                    0\n",
       "runtime                    2\n",
       "spoken_languages           0\n",
       "status                     0\n",
       "tagline                  844\n",
       "title                      0\n",
       "vote_average               0\n",
       "vote_count                 0\n",
       "movie_id                   0\n",
       "cast                       0\n",
       "crew                       0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 148,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "id": "6110daed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>budget</th>\n",
       "      <th>genres</th>\n",
       "      <th>homepage</th>\n",
       "      <th>id</th>\n",
       "      <th>keywords</th>\n",
       "      <th>original_language</th>\n",
       "      <th>original_title</th>\n",
       "      <th>overview</th>\n",
       "      <th>popularity</th>\n",
       "      <th>production_companies</th>\n",
       "      <th>...</th>\n",
       "      <th>runtime</th>\n",
       "      <th>spoken_languages</th>\n",
       "      <th>status</th>\n",
       "      <th>tagline</th>\n",
       "      <th>title</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>vote_count</th>\n",
       "      <th>movie_id</th>\n",
       "      <th>cast</th>\n",
       "      <th>crew</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>62</th>\n",
       "      <td>180000000</td>\n",
       "      <td>[Action, Adventure]</td>\n",
       "      <td>http://legendoftarzan.com</td>\n",
       "      <td>258489</td>\n",
       "      <td>[africa, feral child, tarzan, jungle, animal a...</td>\n",
       "      <td>en</td>\n",
       "      <td>The Legend of Tarzan</td>\n",
       "      <td>Tarzan, having acclimated to life in London, i...</td>\n",
       "      <td>42.741719</td>\n",
       "      <td>[{\"name\": \"Village Roadshow Pictures\", \"id\": 7...</td>\n",
       "      <td>...</td>\n",
       "      <td>109.0</td>\n",
       "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}]</td>\n",
       "      <td>Released</td>\n",
       "      <td>Human. Nature.</td>\n",
       "      <td>The Legend of Tarzan</td>\n",
       "      <td>5.5</td>\n",
       "      <td>2430</td>\n",
       "      <td>258489</td>\n",
       "      <td>[Alexander Skarsgård, Margot Robbie, Christoph...</td>\n",
       "      <td>[David Yates]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2667</th>\n",
       "      <td>14500000</td>\n",
       "      <td>[Drama, Romance]</td>\n",
       "      <td>http://www.romeoandjuliet.com/</td>\n",
       "      <td>454</td>\n",
       "      <td>[shakespeare, forbidden love, gun violence, st...</td>\n",
       "      <td>en</td>\n",
       "      <td>Romeo + Juliet</td>\n",
       "      <td>In director Baz Luhrmann's contemporary take o...</td>\n",
       "      <td>41.493042</td>\n",
       "      <td>[{\"name\": \"Bazmark Films\", \"id\": 240}, {\"name\"...</td>\n",
       "      <td>...</td>\n",
       "      <td>120.0</td>\n",
       "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}]</td>\n",
       "      <td>Released</td>\n",
       "      <td>My only love sprung from my only hate.</td>\n",
       "      <td>Romeo + Juliet</td>\n",
       "      <td>6.7</td>\n",
       "      <td>1374</td>\n",
       "      <td>454</td>\n",
       "      <td>[Leonardo DiCaprio, Claire Danes, John Leguiza...</td>\n",
       "      <td>[Baz Luhrmann]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4210</th>\n",
       "      <td>0</td>\n",
       "      <td>[Drama, Music]</td>\n",
       "      <td>http://www.graceunplugged.com/</td>\n",
       "      <td>206284</td>\n",
       "      <td>[christian]</td>\n",
       "      <td>en</td>\n",
       "      <td>Grace Unplugged</td>\n",
       "      <td>A talented young singer and aspiring songwrite...</td>\n",
       "      <td>2.160586</td>\n",
       "      <td>[{\"name\": \"Coram Deo Studios\", \"id\": 30270}, {...</td>\n",
       "      <td>...</td>\n",
       "      <td>102.0</td>\n",
       "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}]</td>\n",
       "      <td>Released</td>\n",
       "      <td>Would you give up what you need... to get ever...</td>\n",
       "      <td>Grace Unplugged</td>\n",
       "      <td>6.0</td>\n",
       "      <td>24</td>\n",
       "      <td>206284</td>\n",
       "      <td>[AJ Michalka, James Denton, Kevin Pollak, Shaw...</td>\n",
       "      <td>[Brad J. Silverman]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2931</th>\n",
       "      <td>11000000</td>\n",
       "      <td>[Drama]</td>\n",
       "      <td>NaN</td>\n",
       "      <td>687</td>\n",
       "      <td>[prison, rape, socially deprived family, penal...</td>\n",
       "      <td>en</td>\n",
       "      <td>Dead Man Walking</td>\n",
       "      <td>A justice drama based on a true story about a ...</td>\n",
       "      <td>15.864928</td>\n",
       "      <td>[{\"name\": \"Havoc\", \"id\": 406}, {\"name\": \"PolyG...</td>\n",
       "      <td>...</td>\n",
       "      <td>122.0</td>\n",
       "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}]</td>\n",
       "      <td>Released</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dead Man Walking</td>\n",
       "      <td>7.3</td>\n",
       "      <td>337</td>\n",
       "      <td>687</td>\n",
       "      <td>[Susan Sarandon, Sean Penn, Robert Prosky, Ray...</td>\n",
       "      <td>[Tim Robbins]</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>4 rows × 23 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         budget               genres                        homepage      id  \\\n",
       "62    180000000  [Action, Adventure]       http://legendoftarzan.com  258489   \n",
       "2667   14500000     [Drama, Romance]  http://www.romeoandjuliet.com/     454   \n",
       "4210          0       [Drama, Music]  http://www.graceunplugged.com/  206284   \n",
       "2931   11000000              [Drama]                             NaN     687   \n",
       "\n",
       "                                               keywords original_language  \\\n",
       "62    [africa, feral child, tarzan, jungle, animal a...                en   \n",
       "2667  [shakespeare, forbidden love, gun violence, st...                en   \n",
       "4210                                        [christian]                en   \n",
       "2931  [prison, rape, socially deprived family, penal...                en   \n",
       "\n",
       "            original_title                                           overview  \\\n",
       "62    The Legend of Tarzan  Tarzan, having acclimated to life in London, i...   \n",
       "2667        Romeo + Juliet  In director Baz Luhrmann's contemporary take o...   \n",
       "4210       Grace Unplugged  A talented young singer and aspiring songwrite...   \n",
       "2931      Dead Man Walking  A justice drama based on a true story about a ...   \n",
       "\n",
       "      popularity                               production_companies  ...  \\\n",
       "62     42.741719  [{\"name\": \"Village Roadshow Pictures\", \"id\": 7...  ...   \n",
       "2667   41.493042  [{\"name\": \"Bazmark Films\", \"id\": 240}, {\"name\"...  ...   \n",
       "4210    2.160586  [{\"name\": \"Coram Deo Studios\", \"id\": 30270}, {...  ...   \n",
       "2931   15.864928  [{\"name\": \"Havoc\", \"id\": 406}, {\"name\": \"PolyG...  ...   \n",
       "\n",
       "     runtime                          spoken_languages    status  \\\n",
       "62     109.0  [{\"iso_639_1\": \"en\", \"name\": \"English\"}]  Released   \n",
       "2667   120.0  [{\"iso_639_1\": \"en\", \"name\": \"English\"}]  Released   \n",
       "4210   102.0  [{\"iso_639_1\": \"en\", \"name\": \"English\"}]  Released   \n",
       "2931   122.0  [{\"iso_639_1\": \"en\", \"name\": \"English\"}]  Released   \n",
       "\n",
       "                                                tagline                 title  \\\n",
       "62                                       Human. Nature.  The Legend of Tarzan   \n",
       "2667             My only love sprung from my only hate.        Romeo + Juliet   \n",
       "4210  Would you give up what you need... to get ever...       Grace Unplugged   \n",
       "2931                                                NaN      Dead Man Walking   \n",
       "\n",
       "     vote_average vote_count movie_id  \\\n",
       "62            5.5       2430   258489   \n",
       "2667          6.7       1374      454   \n",
       "4210          6.0         24   206284   \n",
       "2931          7.3        337      687   \n",
       "\n",
       "                                                   cast                 crew  \n",
       "62    [Alexander Skarsgård, Margot Robbie, Christoph...        [David Yates]  \n",
       "2667  [Leonardo DiCaprio, Claire Danes, John Leguiza...       [Baz Luhrmann]  \n",
       "4210  [AJ Michalka, James Denton, Kevin Pollak, Shaw...  [Brad J. Silverman]  \n",
       "2931  [Susan Sarandon, Sean Penn, Robert Prosky, Ray...        [Tim Robbins]  \n",
       "\n",
       "[4 rows x 23 columns]"
      ]
     },
     "execution_count": 149,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies.sample(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "id": "a586ec61",
   "metadata": {},
   "outputs": [],
   "source": [
    "def _join(x):\n",
    "  l=[]\n",
    "  for i in x:\n",
    "    l.append(i.replace(\" \",\"\"))\n",
    "  return l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "id": "51bfba80",
   "metadata": {},
   "outputs": [],
   "source": [
    "movies[\"cast\"]=movies[\"cast\"].apply(_join)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "id": "266afc5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "movies[\"cast\"]=movies[\"cast\"].apply(lambda i:i[0:3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "id": "3838bc7e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        [SamWorthington, ZoeSaldana, SigourneyWeaver]\n",
       "1           [JohnnyDepp, OrlandoBloom, KeiraKnightley]\n",
       "2            [DanielCraig, ChristophWaltz, LéaSeydoux]\n",
       "3            [ChristianBale, MichaelCaine, GaryOldman]\n",
       "4          [TaylorKitsch, LynnCollins, SamanthaMorton]\n",
       "                             ...                      \n",
       "4804    [CarlosGallardo, JaimedeHoyos, PeterMarquardt]\n",
       "4805         [EdwardBurns, KerryBishé, MarshaDietlein]\n",
       "4806           [EricMabius, KristinBooth, CrystalLowe]\n",
       "4807            [DanielHenney, ElizaCoupe, BillPaxton]\n",
       "4808    [DrewBarrymore, BrianHerzlinger, CoreyFeldman]\n",
       "Name: cast, Length: 4809, dtype: object"
      ]
     },
     "execution_count": 153,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies[\"cast\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "id": "08500e81",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_df=pd.DataFrame(movies,columns=['id','homepage','title','cast','crew','overview','genres','keywords'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "id": "b5d8ecee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>homepage</th>\n",
       "      <th>title</th>\n",
       "      <th>cast</th>\n",
       "      <th>crew</th>\n",
       "      <th>overview</th>\n",
       "      <th>genres</th>\n",
       "      <th>keywords</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>19995</td>\n",
       "      <td>http://www.avatarmovie.com/</td>\n",
       "      <td>Avatar</td>\n",
       "      <td>[SamWorthington, ZoeSaldana, SigourneyWeaver]</td>\n",
       "      <td>[James Cameron]</td>\n",
       "      <td>In the 22nd century, a paraplegic Marine is di...</td>\n",
       "      <td>[Action, Adventure, Fantasy, Science Fiction]</td>\n",
       "      <td>[culture clash, future, space war, space colon...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>285</td>\n",
       "      <td>http://disney.go.com/disneypictures/pirates/</td>\n",
       "      <td>Pirates of the Caribbean: At World's End</td>\n",
       "      <td>[JohnnyDepp, OrlandoBloom, KeiraKnightley]</td>\n",
       "      <td>[Gore Verbinski]</td>\n",
       "      <td>Captain Barbossa, long believed to be dead, ha...</td>\n",
       "      <td>[Adventure, Fantasy, Action]</td>\n",
       "      <td>[ocean, drug abuse, exotic island, east india ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>206647</td>\n",
       "      <td>http://www.sonypictures.com/movies/spectre/</td>\n",
       "      <td>Spectre</td>\n",
       "      <td>[DanielCraig, ChristophWaltz, LéaSeydoux]</td>\n",
       "      <td>[Sam Mendes]</td>\n",
       "      <td>A cryptic message from Bond’s past sends him o...</td>\n",
       "      <td>[Action, Adventure, Crime]</td>\n",
       "      <td>[spy, based on novel, secret agent, sequel, mi...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>49026</td>\n",
       "      <td>http://www.thedarkknightrises.com/</td>\n",
       "      <td>The Dark Knight Rises</td>\n",
       "      <td>[ChristianBale, MichaelCaine, GaryOldman]</td>\n",
       "      <td>[Christopher Nolan]</td>\n",
       "      <td>Following the death of District Attorney Harve...</td>\n",
       "      <td>[Action, Crime, Drama, Thriller]</td>\n",
       "      <td>[dc comics, crime fighter, terrorist, secret i...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       id                                      homepage  \\\n",
       "0   19995                   http://www.avatarmovie.com/   \n",
       "1     285  http://disney.go.com/disneypictures/pirates/   \n",
       "2  206647   http://www.sonypictures.com/movies/spectre/   \n",
       "3   49026            http://www.thedarkknightrises.com/   \n",
       "\n",
       "                                      title  \\\n",
       "0                                    Avatar   \n",
       "1  Pirates of the Caribbean: At World's End   \n",
       "2                                   Spectre   \n",
       "3                     The Dark Knight Rises   \n",
       "\n",
       "                                            cast                 crew  \\\n",
       "0  [SamWorthington, ZoeSaldana, SigourneyWeaver]      [James Cameron]   \n",
       "1     [JohnnyDepp, OrlandoBloom, KeiraKnightley]     [Gore Verbinski]   \n",
       "2      [DanielCraig, ChristophWaltz, LéaSeydoux]         [Sam Mendes]   \n",
       "3      [ChristianBale, MichaelCaine, GaryOldman]  [Christopher Nolan]   \n",
       "\n",
       "                                            overview  \\\n",
       "0  In the 22nd century, a paraplegic Marine is di...   \n",
       "1  Captain Barbossa, long believed to be dead, ha...   \n",
       "2  A cryptic message from Bond’s past sends him o...   \n",
       "3  Following the death of District Attorney Harve...   \n",
       "\n",
       "                                          genres  \\\n",
       "0  [Action, Adventure, Fantasy, Science Fiction]   \n",
       "1                   [Adventure, Fantasy, Action]   \n",
       "2                     [Action, Adventure, Crime]   \n",
       "3               [Action, Crime, Drama, Thriller]   \n",
       "\n",
       "                                            keywords  \n",
       "0  [culture clash, future, space war, space colon...  \n",
       "1  [ocean, drug abuse, exotic island, east india ...  \n",
       "2  [spy, based on novel, secret agent, sequel, mi...  \n",
       "3  [dc comics, crime fighter, terrorist, secret i...  "
      ]
     },
     "execution_count": 155,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df.head(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "id": "e2b68104",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_df['crew']=new_df['crew'].apply(_join)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "id": "71837f79",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>homepage</th>\n",
       "      <th>title</th>\n",
       "      <th>cast</th>\n",
       "      <th>crew</th>\n",
       "      <th>overview</th>\n",
       "      <th>genres</th>\n",
       "      <th>keywords</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>19995</td>\n",
       "      <td>http://www.avatarmovie.com/</td>\n",
       "      <td>Avatar</td>\n",
       "      <td>[SamWorthington, ZoeSaldana, SigourneyWeaver]</td>\n",
       "      <td>[JamesCameron]</td>\n",
       "      <td>In the 22nd century, a paraplegic Marine is di...</td>\n",
       "      <td>[Action, Adventure, Fantasy, Science Fiction]</td>\n",
       "      <td>[culture clash, future, space war, space colon...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>285</td>\n",
       "      <td>http://disney.go.com/disneypictures/pirates/</td>\n",
       "      <td>Pirates of the Caribbean: At World's End</td>\n",
       "      <td>[JohnnyDepp, OrlandoBloom, KeiraKnightley]</td>\n",
       "      <td>[GoreVerbinski]</td>\n",
       "      <td>Captain Barbossa, long believed to be dead, ha...</td>\n",
       "      <td>[Adventure, Fantasy, Action]</td>\n",
       "      <td>[ocean, drug abuse, exotic island, east india ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>206647</td>\n",
       "      <td>http://www.sonypictures.com/movies/spectre/</td>\n",
       "      <td>Spectre</td>\n",
       "      <td>[DanielCraig, ChristophWaltz, LéaSeydoux]</td>\n",
       "      <td>[SamMendes]</td>\n",
       "      <td>A cryptic message from Bond’s past sends him o...</td>\n",
       "      <td>[Action, Adventure, Crime]</td>\n",
       "      <td>[spy, based on novel, secret agent, sequel, mi...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>49026</td>\n",
       "      <td>http://www.thedarkknightrises.com/</td>\n",
       "      <td>The Dark Knight Rises</td>\n",
       "      <td>[ChristianBale, MichaelCaine, GaryOldman]</td>\n",
       "      <td>[ChristopherNolan]</td>\n",
       "      <td>Following the death of District Attorney Harve...</td>\n",
       "      <td>[Action, Crime, Drama, Thriller]</td>\n",
       "      <td>[dc comics, crime fighter, terrorist, secret i...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>49529</td>\n",
       "      <td>http://movies.disney.com/john-carter</td>\n",
       "      <td>John Carter</td>\n",
       "      <td>[TaylorKitsch, LynnCollins, SamanthaMorton]</td>\n",
       "      <td>[AndrewStanton]</td>\n",
       "      <td>John Carter is a war-weary, former military ca...</td>\n",
       "      <td>[Action, Adventure, Science Fiction]</td>\n",
       "      <td>[based on novel, mars, medallion, space travel...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       id                                      homepage  \\\n",
       "0   19995                   http://www.avatarmovie.com/   \n",
       "1     285  http://disney.go.com/disneypictures/pirates/   \n",
       "2  206647   http://www.sonypictures.com/movies/spectre/   \n",
       "3   49026            http://www.thedarkknightrises.com/   \n",
       "4   49529          http://movies.disney.com/john-carter   \n",
       "\n",
       "                                      title  \\\n",
       "0                                    Avatar   \n",
       "1  Pirates of the Caribbean: At World's End   \n",
       "2                                   Spectre   \n",
       "3                     The Dark Knight Rises   \n",
       "4                               John Carter   \n",
       "\n",
       "                                            cast                crew  \\\n",
       "0  [SamWorthington, ZoeSaldana, SigourneyWeaver]      [JamesCameron]   \n",
       "1     [JohnnyDepp, OrlandoBloom, KeiraKnightley]     [GoreVerbinski]   \n",
       "2      [DanielCraig, ChristophWaltz, LéaSeydoux]         [SamMendes]   \n",
       "3      [ChristianBale, MichaelCaine, GaryOldman]  [ChristopherNolan]   \n",
       "4    [TaylorKitsch, LynnCollins, SamanthaMorton]     [AndrewStanton]   \n",
       "\n",
       "                                            overview  \\\n",
       "0  In the 22nd century, a paraplegic Marine is di...   \n",
       "1  Captain Barbossa, long believed to be dead, ha...   \n",
       "2  A cryptic message from Bond’s past sends him o...   \n",
       "3  Following the death of District Attorney Harve...   \n",
       "4  John Carter is a war-weary, former military ca...   \n",
       "\n",
       "                                          genres  \\\n",
       "0  [Action, Adventure, Fantasy, Science Fiction]   \n",
       "1                   [Adventure, Fantasy, Action]   \n",
       "2                     [Action, Adventure, Crime]   \n",
       "3               [Action, Crime, Drama, Thriller]   \n",
       "4           [Action, Adventure, Science Fiction]   \n",
       "\n",
       "                                            keywords  \n",
       "0  [culture clash, future, space war, space colon...  \n",
       "1  [ocean, drug abuse, exotic island, east india ...  \n",
       "2  [spy, based on novel, secret agent, sequel, mi...  \n",
       "3  [dc comics, crime fighter, terrorist, secret i...  \n",
       "4  [based on novel, mars, medallion, space travel...  "
      ]
     },
     "execution_count": 157,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "id": "e2f4b878",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id             0\n",
       "homepage    3096\n",
       "title          0\n",
       "cast           0\n",
       "crew           0\n",
       "overview       3\n",
       "genres         0\n",
       "keywords       0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 158,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "id": "3fceef4d",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_df[\"homepage\"]=new_df[\"homepage\"].fillna(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "id": "f84a9605",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\acer\\AppData\\Local\\Temp\\ipykernel_3676\\3303242796.py:10: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  new_df[\"urls\"][i]=new_df[\"homepage\"][i]\n"
     ]
    }
   ],
   "source": [
    "url=list(enumerate(new_df[\"homepage\"]))\n",
    "new_df[\"urls\"]=0\n",
    "for i in range(len(url)):\n",
    "  if new_df[\"homepage\"][i]==0:\n",
    "    \n",
    "    x=(\"{}/{}\".format(\"https://www.\",str(\"\".join(list(new_df[\"title\"][url[i][0]].split())))))\n",
    "\n",
    "    new_df[\"urls\"][i]=x\n",
    "  else:\n",
    "    new_df[\"urls\"][i]=new_df[\"homepage\"][i]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "id": "4cf0a6e5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0                             http://www.avatarmovie.com/\n",
       "1            http://disney.go.com/disneypictures/pirates/\n",
       "2             http://www.sonypictures.com/movies/spectre/\n",
       "3                      http://www.thedarkknightrises.com/\n",
       "4                    http://movies.disney.com/john-carter\n",
       "                              ...                        \n",
       "4804                              https://www./ElMariachi\n",
       "4805                               https://www./Newlyweds\n",
       "4806    http://www.hallmarkchannel.com/signedsealeddel...\n",
       "4807                          http://shanghaicalling.com/\n",
       "4808                          https://www./MyDatewithDrew\n",
       "Name: urls, Length: 4809, dtype: object"
      ]
     },
     "execution_count": 161,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df[\"urls\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "id": "4ac18b69",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>homepage</th>\n",
       "      <th>title</th>\n",
       "      <th>cast</th>\n",
       "      <th>crew</th>\n",
       "      <th>overview</th>\n",
       "      <th>genres</th>\n",
       "      <th>keywords</th>\n",
       "      <th>urls</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2369</th>\n",
       "      <td>22102</td>\n",
       "      <td>0</td>\n",
       "      <td>Troop Beverly Hills</td>\n",
       "      <td>[ShelleyLong, CraigT.Nelson, BettyThomas]</td>\n",
       "      <td>[JeffKanew]</td>\n",
       "      <td>A Beverly Hills housewife in the middle of a d...</td>\n",
       "      <td>[Adventure, Comedy, Family]</td>\n",
       "      <td>[wilderness, teen angst]</td>\n",
       "      <td>https://www./TroopBeverlyHills</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4277</th>\n",
       "      <td>27845</td>\n",
       "      <td>0</td>\n",
       "      <td>Trees Lounge</td>\n",
       "      <td>[SteveBuscemi, ChloëSevigny, CarolKane]</td>\n",
       "      <td>[SteveBuscemi]</td>\n",
       "      <td>Tommy has lost his job, his love and his life....</td>\n",
       "      <td>[Comedy, Drama]</td>\n",
       "      <td>[bar, alcoholism, independent film, drinking]</td>\n",
       "      <td>https://www./TreesLounge</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1242</th>\n",
       "      <td>11370</td>\n",
       "      <td>0</td>\n",
       "      <td>The Musketeer</td>\n",
       "      <td>[CatherineDeneuve, MenaSuvari, StephenRea]</td>\n",
       "      <td>[PeterHyams]</td>\n",
       "      <td>In Peter Hyams's adaptation of the famous Alex...</td>\n",
       "      <td>[Action, Adventure, Drama]</td>\n",
       "      <td>[loss of family, queen, power, power takeover,...</td>\n",
       "      <td>https://www./TheMusketeer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4054</th>\n",
       "      <td>74457</td>\n",
       "      <td>0</td>\n",
       "      <td>Redemption Road</td>\n",
       "      <td>[MichaelClarkeDuncan, MorganSimpson, KieleSanc...</td>\n",
       "      <td>[MarioVanPeebles]</td>\n",
       "      <td>A Tennessee-set drama focused on an individual...</td>\n",
       "      <td>[Drama]</td>\n",
       "      <td>[]</td>\n",
       "      <td>https://www./RedemptionRoad</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         id homepage                title  \\\n",
       "2369  22102        0  Troop Beverly Hills   \n",
       "4277  27845        0         Trees Lounge   \n",
       "1242  11370        0        The Musketeer   \n",
       "4054  74457        0      Redemption Road   \n",
       "\n",
       "                                                   cast               crew  \\\n",
       "2369          [ShelleyLong, CraigT.Nelson, BettyThomas]        [JeffKanew]   \n",
       "4277            [SteveBuscemi, ChloëSevigny, CarolKane]     [SteveBuscemi]   \n",
       "1242         [CatherineDeneuve, MenaSuvari, StephenRea]       [PeterHyams]   \n",
       "4054  [MichaelClarkeDuncan, MorganSimpson, KieleSanc...  [MarioVanPeebles]   \n",
       "\n",
       "                                               overview  \\\n",
       "2369  A Beverly Hills housewife in the middle of a d...   \n",
       "4277  Tommy has lost his job, his love and his life....   \n",
       "1242  In Peter Hyams's adaptation of the famous Alex...   \n",
       "4054  A Tennessee-set drama focused on an individual...   \n",
       "\n",
       "                           genres  \\\n",
       "2369  [Adventure, Comedy, Family]   \n",
       "4277              [Comedy, Drama]   \n",
       "1242   [Action, Adventure, Drama]   \n",
       "4054                      [Drama]   \n",
       "\n",
       "                                               keywords  \\\n",
       "2369                           [wilderness, teen angst]   \n",
       "4277      [bar, alcoholism, independent film, drinking]   \n",
       "1242  [loss of family, queen, power, power takeover,...   \n",
       "4054                                                 []   \n",
       "\n",
       "                                urls  \n",
       "2369  https://www./TroopBeverlyHills  \n",
       "4277        https://www./TreesLounge  \n",
       "1242       https://www./TheMusketeer  \n",
       "4054     https://www./RedemptionRoad  "
      ]
     },
     "execution_count": 162,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df.sample(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "id": "98d3dc7d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def spliting(text):\n",
    "  text=str(text).split()\n",
    "  return text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "id": "9a9fe970",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_df['overview']=new_df['overview'].apply(spliting)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "id": "f60d2055",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>title</th>\n",
       "      <th>urls</th>\n",
       "      <th>all_tags</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>19995</td>\n",
       "      <td>Avatar</td>\n",
       "      <td>http://www.avatarmovie.com/</td>\n",
       "      <td>[In, the, 22nd, century,, a, paraplegic, Marin...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>285</td>\n",
       "      <td>Pirates of the Caribbean: At World's End</td>\n",
       "      <td>http://disney.go.com/disneypictures/pirates/</td>\n",
       "      <td>[Captain, Barbossa,, long, believed, to, be, d...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>206647</td>\n",
       "      <td>Spectre</td>\n",
       "      <td>http://www.sonypictures.com/movies/spectre/</td>\n",
       "      <td>[A, cryptic, message, from, Bond’s, past, send...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>49026</td>\n",
       "      <td>The Dark Knight Rises</td>\n",
       "      <td>http://www.thedarkknightrises.com/</td>\n",
       "      <td>[Following, the, death, of, District, Attorney...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>49529</td>\n",
       "      <td>John Carter</td>\n",
       "      <td>http://movies.disney.com/john-carter</td>\n",
       "      <td>[John, Carter, is, a, war-weary,, former, mili...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       id                                     title  \\\n",
       "0   19995                                    Avatar   \n",
       "1     285  Pirates of the Caribbean: At World's End   \n",
       "2  206647                                   Spectre   \n",
       "3   49026                     The Dark Knight Rises   \n",
       "4   49529                               John Carter   \n",
       "\n",
       "                                           urls  \\\n",
       "0                   http://www.avatarmovie.com/   \n",
       "1  http://disney.go.com/disneypictures/pirates/   \n",
       "2   http://www.sonypictures.com/movies/spectre/   \n",
       "3            http://www.thedarkknightrises.com/   \n",
       "4          http://movies.disney.com/john-carter   \n",
       "\n",
       "                                            all_tags  \n",
       "0  [In, the, 22nd, century,, a, paraplegic, Marin...  \n",
       "1  [Captain, Barbossa,, long, believed, to, be, d...  \n",
       "2  [A, cryptic, message, from, Bond’s, past, send...  \n",
       "3  [Following, the, death, of, District, Attorney...  \n",
       "4  [John, Carter, is, a, war-weary,, former, mili...  "
      ]
     },
     "execution_count": 165,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df['all_tags']=new_df['overview'] + new_df['genres'] + new_df['keywords'] + new_df['cast'] + new_df['crew']\n",
    "     \n",
    "new_df.drop(columns=['overview','genres' ,'keywords','cast' , 'crew','homepage'],inplace=True)\n",
    "     \n",
    "new_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "id": "ca4dc2fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "def convert_lower(text):\n",
    "  l=[]\n",
    "  for item in text:\n",
    "    l.append(item.lower())\n",
    "  return l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "id": "efc6885d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>title</th>\n",
       "      <th>urls</th>\n",
       "      <th>all_tags</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>19995</td>\n",
       "      <td>Avatar</td>\n",
       "      <td>http://www.avatarmovie.com/</td>\n",
       "      <td>[in, the, 22nd, century,, a, paraplegic, marin...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>285</td>\n",
       "      <td>Pirates of the Caribbean: At World's End</td>\n",
       "      <td>http://disney.go.com/disneypictures/pirates/</td>\n",
       "      <td>[captain, barbossa,, long, believed, to, be, d...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>206647</td>\n",
       "      <td>Spectre</td>\n",
       "      <td>http://www.sonypictures.com/movies/spectre/</td>\n",
       "      <td>[a, cryptic, message, from, bond’s, past, send...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>49026</td>\n",
       "      <td>The Dark Knight Rises</td>\n",
       "      <td>http://www.thedarkknightrises.com/</td>\n",
       "      <td>[following, the, death, of, district, attorney...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>49529</td>\n",
       "      <td>John Carter</td>\n",
       "      <td>http://movies.disney.com/john-carter</td>\n",
       "      <td>[john, carter, is, a, war-weary,, former, mili...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       id                                     title  \\\n",
       "0   19995                                    Avatar   \n",
       "1     285  Pirates of the Caribbean: At World's End   \n",
       "2  206647                                   Spectre   \n",
       "3   49026                     The Dark Knight Rises   \n",
       "4   49529                               John Carter   \n",
       "\n",
       "                                           urls  \\\n",
       "0                   http://www.avatarmovie.com/   \n",
       "1  http://disney.go.com/disneypictures/pirates/   \n",
       "2   http://www.sonypictures.com/movies/spectre/   \n",
       "3            http://www.thedarkknightrises.com/   \n",
       "4          http://movies.disney.com/john-carter   \n",
       "\n",
       "                                            all_tags  \n",
       "0  [in, the, 22nd, century,, a, paraplegic, marin...  \n",
       "1  [captain, barbossa,, long, believed, to, be, d...  \n",
       "2  [a, cryptic, message, from, bond’s, past, send...  \n",
       "3  [following, the, death, of, district, attorney...  \n",
       "4  [john, carter, is, a, war-weary,, former, mili...  "
      ]
     },
     "execution_count": 167,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df['all_tags']=new_df['all_tags'].apply(convert_lower)\n",
    "     \n",
    "new_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "id": "18910b42",
   "metadata": {},
   "outputs": [],
   "source": [
    "import nltk\n",
    "from nltk.stem.porter import PorterStemmer\n",
    "ps=PorterStemmer()\n",
    "def steming(text):\n",
    "  l=[]\n",
    "  for i in text:\n",
    "\n",
    "    l.append(ps.stem(i))\n",
    "  return l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "id": "69588dec",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>title</th>\n",
       "      <th>urls</th>\n",
       "      <th>all_tags</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2870</th>\n",
       "      <td>60599</td>\n",
       "      <td>Arbitrage</td>\n",
       "      <td>https://www./Arbitrage</td>\n",
       "      <td>[a, troubl, hedg, fund, magnate,, desper, to, ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2942</th>\n",
       "      <td>14369</td>\n",
       "      <td>Out Cold</td>\n",
       "      <td>https://www./OutCold</td>\n",
       "      <td>[anim, hous, meet, casablanca, in, thi, outrag...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3982</th>\n",
       "      <td>248</td>\n",
       "      <td>Pocketful of Miracles</td>\n",
       "      <td>https://www./PocketfulofMiracles</td>\n",
       "      <td>[damon, runyon', fairytale,, sweet, and, funny...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1317</th>\n",
       "      <td>11306</td>\n",
       "      <td>Extreme Measures</td>\n",
       "      <td>https://www./ExtremeMeasures</td>\n",
       "      <td>[thriller, about, guy, luthan, (hugh, grant),,...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2749</th>\n",
       "      <td>1954</td>\n",
       "      <td>The Butterfly Effect</td>\n",
       "      <td>https://www./TheButterflyEffect</td>\n",
       "      <td>[a, young, man, struggl, to, access, sublim, c...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         id                  title                              urls  \\\n",
       "2870  60599              Arbitrage            https://www./Arbitrage   \n",
       "2942  14369               Out Cold              https://www./OutCold   \n",
       "3982    248  Pocketful of Miracles  https://www./PocketfulofMiracles   \n",
       "1317  11306       Extreme Measures      https://www./ExtremeMeasures   \n",
       "2749   1954   The Butterfly Effect   https://www./TheButterflyEffect   \n",
       "\n",
       "                                               all_tags  \n",
       "2870  [a, troubl, hedg, fund, magnate,, desper, to, ...  \n",
       "2942  [anim, hous, meet, casablanca, in, thi, outrag...  \n",
       "3982  [damon, runyon', fairytale,, sweet, and, funny...  \n",
       "1317  [thriller, about, guy, luthan, (hugh, grant),,...  \n",
       "2749  [a, young, man, struggl, to, access, sublim, c...  "
      ]
     },
     "execution_count": 169,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df['all_tags']=new_df['all_tags'].apply(steming)\n",
    "     \n",
    "new_df.sample(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "id": "8c17d3a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_df[\"all_tags\"]=new_df[\"all_tags\"].apply(_join)\n",
    "     \n",
    "new_df['all_tags'] = new_df['all_tags'].apply(lambda x: \" \".join(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "id": "e25a1cae",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "cv = CountVectorizer(stop_words='english')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "id": "8cb2a7f8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0, 0, 0, ..., 0, 0, 0],\n",
       "       [0, 0, 0, ..., 0, 0, 0],\n",
       "       [0, 0, 0, ..., 0, 0, 0],\n",
       "       ...,\n",
       "       [0, 0, 0, ..., 0, 0, 0],\n",
       "       [0, 0, 0, ..., 0, 0, 0],\n",
       "       [0, 0, 0, ..., 0, 0, 0]], dtype=int64)"
      ]
     },
     "execution_count": 172,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = cv.fit_transform(new_df['all_tags']).toarray()\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "id": "916377f2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1.        , 0.06776309, 0.06862635, ..., 0.03571429, 0.        ,\n",
       "        0.        ],\n",
       "       [0.06776309, 1.        , 0.05063697, ..., 0.01976424, 0.        ,\n",
       "        0.0209427 ],\n",
       "       [0.06862635, 0.05063697, 1.        , ..., 0.02001602, 0.        ,\n",
       "        0.        ],\n",
       "       ...,\n",
       "       [0.03571429, 0.01976424, 0.02001602, ..., 1.        , 0.03311331,\n",
       "        0.03311331],\n",
       "       [0.        , 0.        , 0.        , ..., 0.03311331, 1.        ,\n",
       "        0.07017544],\n",
       "       [0.        , 0.0209427 , 0.        , ..., 0.03311331, 0.07017544,\n",
       "        1.        ]])"
      ]
     },
     "execution_count": 177,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics.pairwise import cosine_similarity\n",
    "similarity = cosine_similarity(data)\n",
    "similarity"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "id": "94f56806",
   "metadata": {},
   "outputs": [],
   "source": [
    "def movie_recommend(movie):\n",
    "    index = new_df[new_df['title'] == movie].index[0]\n",
    "    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])\n",
    "    for i in distances[1:8]:\n",
    "\n",
    "      \n",
    "      print(\"{} {}\".format(new_df.iloc[i[0]].title,new_df.iloc[i[0]].urls))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "id": "a779f3ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Aliens https://www./Aliens\n",
      "Aliens vs Predator: Requiem http://www.avp-r.com/\n",
      "Titan A.E. https://www./TitanA.E.\n",
      "Independence Day https://www./IndependenceDay\n",
      "Battle: Los Angeles http://www.battlela.com\n",
      "Meet Dave http://www.meetdavemovie.com/\n",
      "Predators https://www./Predators\n"
     ]
    }
   ],
   "source": [
    "movie_recommend(\"Avatar\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "id": "f97af28b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Batman https://www./Batman\n",
      "Batman & Robin https://www./Batman&Robin\n",
      "The R.M. http://www.halestormentertainment.com/p_movies_details.asp?mID=jnlppmp8\n",
      "Batman Begins http://www2.warnerbros.com/batmanbegins/index.html\n",
      "Batman Returns https://www./BatmanReturns\n",
      "The Dark Knight http://thedarkknight.warnerbros.com/dvdsite/\n",
      "The Dark Knight Rises http://www.thedarkknightrises.com/\n"
     ]
    }
   ],
   "source": [
    "movie_recommend(\"Batman\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "id": "374bd7b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "id": "e4c05d0a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Avatar', \"Pirates of the Caribbean: At World's End\", 'Spectre',\n",
       "       ..., 'Signed, Sealed, Delivered', 'Shanghai Calling',\n",
       "       'My Date with Drew'], dtype=object)"
      ]
     },
     "execution_count": 182,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pickle.dump(new_df,open(\"movie_recm.pkl\",\"wb\"))\n",
    "pickle.dump(similarity,open(\"similarity.pkl\",\"wb\"))\n",
    "     \n",
    "np.array(new_df[\"title\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bd085698",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
