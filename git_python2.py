{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "faee61f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate_factorial(n):\n",
    "    if n == 0:\n",
    "        return 1\n",
    "    else:\n",
    "        factorial = 1\n",
    "        index = 1\n",
    "        while index <= n:\n",
    "            factorial = factorial * index\n",
    "            index += 1\n",
    "        return factorial"
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
