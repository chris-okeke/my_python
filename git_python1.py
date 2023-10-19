{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6d124c38",
   "metadata": {},
   "outputs": [],
   "source": [
    "def print_number(n):\n",
    "    if n <= 0:\n",
    "        print(\"Please enter a positive number! \")\n",
    "    current_number = 1\n",
    "    while current_number <= n:\n",
    "        print(current_number)\n",
    "        current_number += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "17d019a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "def print_even_number(n):\n",
    "    if n < 2:\n",
    "        print(\"please enter a valid number, must be greater than 2\")\n",
    "    x = 2\n",
    "    while x <= n:\n",
    "        print(x)\n",
    "        x += 2"
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
