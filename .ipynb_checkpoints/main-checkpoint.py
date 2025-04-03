{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "88ad5c28-4803-4d1f-8b3b-636220750c74",
   "metadata": {},
   "outputs": [],
   "source": [
    "op=input(\"Enter any of the operator +,*,even,integer\")\n",
    "list=[27,34,23,-21,22,3.2]\n",
    "\n",
    "def main(op,list):\n",
    "    print(\"Hello learners!\")\n",
    "    if op==\"+\":\n",
    "        addmultiplenumbers(list)\n",
    "    elif op==\"*\":\n",
    "        multiplymultiplenumbers(list)\n",
    "    elif op==\"even\":\n",
    "        num=float(input(\"Enter a number to check whether it is even or not\"))\n",
    "        print(isiteven(num))\n",
    "    elif op==\"integer\":\n",
    "        num=float(input(\"Enter a value to check whether it is integer or not\"))\n",
    "        print(isitaninteger(num))\n",
    "    else:\n",
    "        print(\"Enter a valid number or operator\")\n",
    "\n",
    "def addmultiplenumbers(list):\n",
    "    sum=0\n",
    "    for i in list:\n",
    "        sum=sum+i\n",
    "    print(\"The sum of three numbers is\", sum)\n",
    "  \n",
    "def multiplymultiplenumbers(list):\n",
    "    mul=1\n",
    "    for i in list:\n",
    "        mul=mul*i\n",
    "    print(\"The multiplication of three numbers is\",mul)\n",
    "\n",
    "def isiteven(num):\n",
    "    if num%2==0:\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "\n",
    "def isitaninteger(num):\n",
    "    if num==int(num):\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "\n",
    "main(op,list)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "54224db9-305a-4d6d-bda5-00db86e16369",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\u001b[33m\u001b[33mno tests ran\u001b[0m\u001b[33m in 0.01s\u001b[0m\u001b[0m\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\u001b[31mERROR: found no collectors for C:\\Users\\arulr\\DA course\\Python\\Calculator assessment.ipynb\n",
      "\u001b[0m\n"
     ]
    }
   ],
   "source": [
    "!pytest \"Calculator assessment.ipynb\" -q --tb=line\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5f56caeb-a738-4707-bd1c-788fe4cff130",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "=================================== ERRORS ====================================\n",
      "\u001b[31m\u001b[1m__________________________ ERROR collecting test.py ___________________________\u001b[0m\n",
      "\u001b[31mImportError while importing test module 'C:\\Users\\arulr\\DA course\\Python\\test.py'.\n",
      "Hint: make sure your test modules/packages have valid Python names.\n",
      "Traceback:\n",
      "\u001b[1m\u001b[31m..\\..\\anaconda3\\Lib\\importlib\\__init__.py\u001b[0m:90: in import_module\n",
      "    \u001b[94mreturn\u001b[39;49;00m _bootstrap._gcd_import(name[level:], package, level)\u001b[90m\u001b[39;49;00m\n",
      "\u001b[1m\u001b[31mtest.py\u001b[0m:1: in <module>\n",
      "    \u001b[94mfrom\u001b[39;49;00m \u001b[04m\u001b[96mmain\u001b[39;49;00m \u001b[94mimport\u001b[39;49;00m addmultiplenumbers, multiplymultiplenumbers, isiteven, isitaninteger\u001b[90m\u001b[39;49;00m\n",
      "\u001b[1m\u001b[31mE   ModuleNotFoundError: No module named 'main'\u001b[0m\u001b[0m\n",
      "\u001b[36m\u001b[1m=========================== short test summary info ===========================\u001b[0m\n",
      "\u001b[31mERROR\u001b[0m test.py\n",
      "!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!\n",
      "\u001b[31m\u001b[31m\u001b[1m1 error\u001b[0m\u001b[31m in 0.26s\u001b[0m\u001b[0m\n"
     ]
    }
   ],
   "source": [
    "!pytest test.py -q --tb=line"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a793982a-b511-4a5b-98ce-3bafee4bfb8a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "=================================== ERRORS ====================================\n",
      "\u001b[31m\u001b[1m__________________________ ERROR collecting test.py ___________________________\u001b[0m\n",
      "\u001b[31mImportError while importing test module 'C:\\Users\\arulr\\DA course\\Python\\test.py'.\n",
      "Hint: make sure your test modules/packages have valid Python names.\n",
      "Traceback:\n",
      "\u001b[1m\u001b[31m..\\..\\anaconda3\\Lib\\importlib\\__init__.py\u001b[0m:90: in import_module\n",
      "    \u001b[94mreturn\u001b[39;49;00m _bootstrap._gcd_import(name[level:], package, level)\u001b[90m\u001b[39;49;00m\n",
      "\u001b[1m\u001b[31mtest.py\u001b[0m:1: in <module>\n",
      "    \u001b[94mfrom\u001b[39;49;00m \u001b[04m\u001b[96mmain\u001b[39;49;00m\u001b[04m\u001b[96m.\u001b[39;49;00m\u001b[04m\u001b[96mipynb\u001b[39;49;00m \u001b[94mimport\u001b[39;49;00m addmultiplenumbers, multiplymultiplenumbers, isiteven, isitaninteger\u001b[90m\u001b[39;49;00m\n",
      "\u001b[1m\u001b[31mE   ModuleNotFoundError: No module named 'main'\u001b[0m\u001b[0m\n",
      "\u001b[36m\u001b[1m=========================== short test summary info ===========================\u001b[0m\n",
      "\u001b[31mERROR\u001b[0m test.py\n",
      "!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!\n",
      "\u001b[31m\u001b[31m\u001b[1m1 error\u001b[0m\u001b[31m in 0.27s\u001b[0m\u001b[0m\n"
     ]
    }
   ],
   "source": [
    "!pytest test.py -q --tb=line"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f2fd7ba9-2e24-4734-8027-381e4ce3062f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
