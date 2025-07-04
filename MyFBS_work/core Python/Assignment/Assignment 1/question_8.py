#8.Write a program to convert days into years, weeks and days. 
days=1000
years=days//365
days=days%365
weeks=days//7
days=days%7
print("years:",years,"weeks:",weeks,"days:",days)
