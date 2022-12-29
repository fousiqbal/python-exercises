{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.0"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# program to print 5% of ath sum of given integers\n",
    "\n",
    "def myfunc(a,b):\n",
    "     return(a+b)*0.05\n",
    "myfunc(10,30)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "27.5"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def myfunc(*args):\n",
    "    return sum(args)*0.05\n",
    "myfunc(10,20,30,40,50,60,70,80,90,100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)\n"
     ]
    }
   ],
   "source": [
    "def myfunc(*args):\n",
    "    print(args)\n",
    "myfunc(10,20,30,40,50,60,70,80,90,100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "20\n",
      "30\n",
      "40\n",
      "50\n",
      "60\n",
      "70\n",
      "80\n",
      "90\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "def myfunc(*args):\n",
    "    for item in args:\n",
    "        print(item)\n",
    "myfunc(10,20,30,40,50,60,70,80,90,100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'aPpLe'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#write a program to display it in uppercase in even places and lowercase in odd places\n",
    "\n",
    "def myfunc(word):\n",
    "   \n",
    "    result = \"\"\n",
    "    index = 0\n",
    "    for letter in word:\n",
    "        if index % 2 == 0:\n",
    "            result += letter.lower()\n",
    "        else:\n",
    "            result += letter.upper()\n",
    "        index += 1\n",
    "    return result\n",
    "myfunc(\"apple\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Write a program to display the lesser of 2 even numbers else return the highest digit\n",
    "\n",
    "def lesser_of_two_evens(a,b):\n",
    "    if a % 2 == 0 and b % 2 == 0:\n",
    "        if a < b:\n",
    "            result = a\n",
    "        else:\n",
    "            result = b\n",
    "    else:\n",
    "        if a > b:\n",
    "            result = a\n",
    "        else:\n",
    "            result = b\n",
    "    return result\n",
    "lesser_of_two_evens(2,5)\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#write a program that return true if the words start with same letter else return false \n",
    "\n",
    "def animal_crackers(text):\n",
    "    wordlist = text.split()\n",
    "    return wordlist[0][0] == wordlist[1][0]\n",
    "animal_crackers(\"Lion, Lepord\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#write a program that returns true if the sum of 2 digits or the digit itself is 20\n",
    "\n",
    "def makes_twenty(a,b):\n",
    "    return (a+b)==20 or a==20 or b==20\n",
    "makes_twenty(20,18)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'ProGramming'"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Write a program to display the first and forth letters of a word in uppercase\n",
    "\n",
    "def capital(name):\n",
    "    first_letter = name[0]\n",
    "    inbetween = name[1:3]\n",
    "    last_letter = name[3]\n",
    "    rest = name[4:]\n",
    "    return first_letter.upper() + inbetween + last_letter.upper() + rest\n",
    "capital(\"programming\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "161"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Define a function called myfunc that takes in an arbitrary number of arguments, and returns the sum of those arguments.\n",
    "\n",
    "def myfunc(*args):\n",
    "    return sum (args)\n",
    "myfunc(3,58,98,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 4, 6, 8]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Define a function called myfunc that takes in an arbitrary number of arguments, and returns a list containing only those arguments that are even.\n",
    "\n",
    "def myfunc(*args):\n",
    "      my_list = []\n",
    "      for num in args:\n",
    "        if num % 2 == 0:\n",
    "            my_list.append(num)\n",
    "        else:\n",
    "            pass\n",
    "      return (my_list)\n",
    "myfunc(1,2,3,4,5,6,7,8,9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'mIsSiSiPpI'"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase. \n",
    "\n",
    "\n",
    "def myfunc(word):\n",
    "    result = \"\"\n",
    "    index = 0\n",
    "    for letter in word:\n",
    "        if index % 2 == 0:\n",
    "            result += letter.lower()\n",
    "        else:\n",
    "            result += letter.upper()\n",
    "        index += 1\n",
    "    return result\n",
    "myfunc(\"missisippi\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#write a program to return true if two 3's are adjacent, else return false\n",
    "\n",
    "\n",
    "def has_33(nums):\n",
    "    for i in range(0,len(nums)-1):\n",
    "        if nums[i]==3 and nums[i+1]==3:\n",
    "            return True\n",
    "    return False\n",
    "has_33([1,3,1,3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'MMMiiissssssiiisssiiippppppiii'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#write a program to return a letter 3 times in a word\n",
    "\n",
    "def paper_doll(text):\n",
    "    result = ''\n",
    "    for char in text:\n",
    "        result+= char*3\n",
    "    return result\n",
    "paper_doll(\"Hello\")\n",
    "paper_doll(\"Missisippi\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "18"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#write a program to play blackjack\n",
    "\n",
    "def blackjack(a,b,c):\n",
    "    if sum([a,b,c]) <= 21:\n",
    "        return sum([a,b,c])\n",
    "    elif 11 in [a,b,c] and sum([a,b,c])-10 <= 21:\n",
    "        return sum([a,b,c])-10\n",
    "    else:\n",
    "        return \"Bust\"\n",
    "blackjack(5,2,11)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
