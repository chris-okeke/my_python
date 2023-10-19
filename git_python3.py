{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fdc01342",
   "metadata": {},
   "outputs": [],
   "source": [
    "teams = [\"Man utd\", \"Chelsea\", \"Arsenal\",\"Liverpool\"]\n",
    "for home_team in (teams):\n",
    "    for away_team in (teams):\n",
    "        if home_team != away_team:\n",
    "            print(home_team + \" VS \" + away_team)\n",
    "    "
   ]
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
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
