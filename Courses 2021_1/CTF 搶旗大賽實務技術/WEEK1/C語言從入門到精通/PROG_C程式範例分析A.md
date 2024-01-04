
```
C語言從入門到精通（项目案例版）
明日科技  清華大學  2017
```
```
//3.3
#include<stdio.h>
main()
{
printf("12\t34\r56\n7     8\b9 10");
printf("\n\052,\x26");
}


```

```
//3.4
#include<stdio.h>
main()
{
char c1,c2;
c1='a';						
c2='b'; 						
c1=c1+10;
c2=c2-c1+10;
printf("%c,%d\n%c,%d",c1,c1,c2,c2);
}

```

```
//3.5
#include<stdio.h>
main()
{
  char ch1,ch2;
  ch1='a'; ch2='B';							
  printf("ch1=%c,ch2=%c\n",ch1-32,ch2+32);		
  printf("ch1+10=%d\n", ch1+10);
  printf("ch1+10=%c\n", ch1+10);
  printf("ch2+10=%d\n", ch2+10);
  printf("ch2+10=%c\n", ch2+10);
}


```

```
//3.6
#include<stdio.h>
main()
{
float i,j;
int k;
printf("please input:\n");
scanf("%f,%f",&i,&j);
k=(int)i%(int)j; 						
printf("%d",k);
}


```
```
//3.7
#include <stdio.h>
main()
{
    int i, j;
    i = 3.14159;
    j = 5.99;
    printf("%d\n%d\n", i, j);
    printf("%f\n%f", (float)i, (float)j);
}



```

```
//3.8
#include<stdio.h>
main()
{
int a;
printf("please input:\n");
scanf("%d",&a);
a+=a*=a/=a-6;
printf("the result is %d\n",a);
}


```

```
//3.9
#include<stdio.h>
main()
{
int a,b,r1,r2,r3,r4,r5;
printf("please input:\n");
scanf("%d,%d",&a,&b);
r1=a+b;
r2=a-b;
r3=a*b;
r4=a/b;
r5=a%b;
printf("a+b=%d\n",r1);
printf("a-b=%d\n",r2);
printf("a*b=%d\n",r3);
printf("a/b=%d\n",r4);
printf("a mod b=%d\n",r5);
}


```

```
//3.10
#include<stdio.h>
main()
{
int i=5,x1,x2,x3,x4;
x1=i++;
x2=++i;
x3=i--;
x4=--i;
printf("%d,%d,%d,%d",x1,x2,x3,x4);
}


```

```
//3.11
#include<stdio.h>
main()
{
int a=5,b=10,c=8,d=6,x1,x2,x3;
x1=a>b>d;
x2=a>(b>d);
x3=a+b>c+d;
printf("%d,%d,%d",x1,x2,x3);
}


```

```
//3.12
#include<stdio.h>
main()
{
int i=5,j=8,k=12,l=4,x1,x2;
x1=i>j&&k>l;
x2=!(i>j)&&k>l;
printf("%d,%d",x1,x2);
}


```
```
//3.13
#include<stdio.h>
main()
{
int a=4,b=6,c=8,res1,res2;
res1=a+b,res2=b+c;
printf("y=%d,x=%d",res1,res2);
}


```
```
//4.1
#include<stdio.h>
int palind(char str[],int k, int i)							
{
  if(str[k]==str[i-k]&&k==0)								
    return 1;
  else if(str[k]==str[i-k])									
    palind(str,k-1,i);   									
  else
    return 0;
}
main()
{
  int i=0,n=0;											
  char ch,str[20];
  while ((ch=getchar())!='\n')
    {
      str[i]=ch;
      i++;
    }
  if(i%2==0)											
    n=palind(str,(i/2),i-1);
  else
    n=palind(str,(i/2-1),i-1);								
  if(n==0)
    printf("not palindrome");								
  else
    printf("palindrome");
  getch();
}


```
```
//4.2
#include<stdio.h>
main()
{
char a,b,c,d;
a='h';
b='e';
c='l';
d='o';
putchar(a);
putchar(b);
putchar(c);
putchar(c);
putchar(d);
}


```
```
//4.3
#include<stdio.h>
main()
{
char a,b;
a=getchar();
b=getchar();
putchar('\n');
putchar(a);
putchar(b);
}


```
```
//4.4
#include<stdio.h>
main()
{
int i,k;
long j;
i=36;
j=42767;
k=123;
printf("%d,%d\n",i,k);
printf("%4d,%2d\n",i,k);
printf("%ld",j);
}


```
```
//4.5
#include<stdio.h>
main()
{
int i=32;
printf("%d,%o",i,i);
}


```
```
//4.6
#include<stdio.h>
main()
{
	int i=32;
	printf("%d,%o,%x",i,i,i); 					
}


```
```
//4.7
#include<stdio.h>
main()
{
int i,j;
i=32768,j=32767;
printf("%d,%d\n",i,j);
printf("%u,%u",i,j);
}


```
```
//4.8
#include<stdio.h>
main()
{
int i=99;
char ch='a';
printf("%d,%c",ch,i);
}


```
```
//4.9
#include<stdio.h>
main()
{
char *str="helloworld";
printf("%s\n%10.5s\n%-10.2s\n%.3s",str,str,str,str);
}


```
```
//4.10
#include<stdio.h>
main()
{
float i=2998.453257845;
double j=2998.453257845;
printf("%f\n%15.2f\n%-10.3f\n%f",i,i,i,j); 				
}


```
```
//4.11
#include<stdio.h>
main()
{
float i=2998.453257845;
double j=2998.453257845;
printf("%e\n%15.2e\n%-10.3e\n%e",i,i,i,j);
}


```
```
//4.12
#include<stdio.h>
main()
{
int x,y,m,n;
scanf("%d,%d",&x,&y);
scanf("%d%d",&m,&n);
printf("x is %d,y is %d\n",x,y);
printf("m is %d,n is %d\n",m,n);
}


```
```
//4.13
#include<stdio.h>
main()
{
int a,b,c,d,e;
scanf("%d%d",&a,&b);
scanf("%d%d%d",&c,&d,&e);
printf("the result is:\n");
printf("%d,%d,%d,%d,%d",a,b,c,d,e);
}


```
```
//4.14
#include <stdio.h>
#include <math.h>
main()
{
    float a, b, c;
    printf("please input two orthogonal sides:\n");
    scanf("%f,%f", &a, &b);								
    c = hypot(a, b);										
    printf("hypotenuse is:%f\n", c);							
    getch();
}


```
```
//4.15
#include<stdio.h>
main()
{
    float a1 = 3, b1 = 1, c1 = 4, d1 = 5;							
    float day;												 
    day = 1 / (1 / a1 + 1 / b1 + 1 / c1 + 1 / d1);
        													
    printf("need %f day!", day);									 
} 


```
```
//4.16
#include<stdio.h>
main()
{
char ch;
ch=getchar();
printf("lowercase is %c\n",ch);
ch=ch-32;
printf("majuscule is %c\n",ch);
}


```
```
//4.17
#include <stdio.h>
main()
{
    int a, b, c, t;								
    clrscr(); 
    printf("please input a,b,c:\n");					 
    scanf("%d%d%d", &a, &b, &c);					 
    if (a > b)									
    {
        t = a;
        a = b;
        b = t;
    }
    if (a > c)									 
    {
        t = a;
        a = c;
        c = t;
    }
    if (b > c)								
    {
        t = b;
        b = c;
        c = t;
    }
    printf("the order of the number is:\n");
    printf("%d,%d,%d", a, b, c);						
}


```
```
//4.18
#include <stdio.h>
main()
{
    int year;											
    printf("please input the year:\n");
    scanf("%d", &year);									
    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)		
        printf("%d is a leap year", year);						 
    else
        printf("%d is not a leap year", year);					
}


```
```
//4.19
#include<stdio.h>
main()
{
    int x;
    printf("please input a number:\n");
    scanf("%d", &x); 										
    if (x % 5 == 0 && x % 7 == 0)								
        printf("yes");									
    else
        printf("no");										
}


```
```
//4.20
#include<stdio.h>
main()
{
int x;
printf("please input a number:\n");
scanf("%d",&x);
(x%5==0&&x%7==0)?printf("yes"):printf("no");						


```
```
//4.21
#include<stdio.h>
main()
{
    int score;
    printf("\nplease enter score(score<=100):");
    scanf("%d", &score); 									
    if (score == 100)										
        score = 90;
    score = score / 10; 								
    switch (score)
    {
        case 9:
            printf("the grade is A"); 						
            break;
        case 8:
            printf("the grade is B"); 						
            break;
        case 7:
            printf("the grade is C"); 						
            break;
        case 6:
            printf("the grade is D"); 					
            break;
        default:
            printf("the grade is E"); 						
    }
}


```
```
//4.22
#include<stdio.h>
main()
{
    int score;
    printf("\nplease enter score(score<=100):");
    scanf("%d", &score); 									
    if (score == 100)										
        score = 90;
    score = score / 10; 									
    switch (score)
    {
        case 9:
    printf("the grade is A\n"); 						
        case 8:
    printf("the grade is B\n"); 						
        case 7:
    printf("the grade is C\n"); 						
        case 6:
    printf("the grade is D\n"); 						
        default:
    printf("the grade is E\n"); 						
    }
}


```
```
//4.23
#include <stdio.h>
#include <math.h>
main()
{
    float a, b, c;
    float s, area;
    scanf("%f,%f,%f", &a, &b, &c);
    if (a + b > c && b + c > a && a + c > b)						
    {
        s = (a + b + c) / 2;
        area = sqrt(s *(s - a)*(s - b)*(s - c)); 						
        printf("the area is:%f\n", area); 							
        if (a == b && a == c)								
            printf("equilateral triangle\n");
         											
        else if (a == b || a == c || b == c)
         												
            printf("isoceles triangle\n");
         											
        else if ((a *a + b * b == c *c) || (a *a + c * c == b *b) || (b *b + c* c == a *a))
     
            printf("right angled triangle\n");						
        else
            printf("triangle");									
    }
    else
        printf("can not compose triangle");
    
}


```
```
//4.24
#include <stdio.h>
main()
{
    float x, m1, m2, m;
    char y, z;
    scanf("%f,%c,%c", &x, &y, &z); 							
    switch (y)
    {
        case 'a':
            m1 = 3.25;
            break;
        case 'b':
            m1 = 3.00;
            break;
        case 'c':
            m1 = 2.75;
            break;
    }
    switch (z)
    {
        case 'a':
            m2 = 0;
            break;
        case 'm':
            m2 = 0.05;
            break;
        case 'e':
            m2 = 0.1;
            break;
    }
    m = x * m1 - x * m1 * m2; 									
    printf("the type of oil is:%c\n", y);
    printf("the type of server is:%c\n", z);
    printf("the money is:%.3f", m);
}


```

```
//5.1
#include<stdio.h>
main()
{
    int i = 1; 							
    double sum = 0; 						
    while (i <21)						
    {
        sum = sum + 1.0 / (double)i;
        i++;
    }
    printf("sum=%lf\n",sum); 			
} 


```
```
//5.2
#include<stdio.h>
 main()
       {
         int n,i;
         long int fac;
	 printf("please input n (n>=0) :");
         scanf("%d",&n) ;
         if (n>=0)
           {
            fac = 1 ;
              if (n>0)
               {
                     i =1;
                      while(i<=n)
                    {
                       fac*= i ;
                       i=i+1;
                      }
               }
          printf("%d! = %ld \n",n,fac);
            }
	  else
              printf("error\n");
     }


```
```
//5.3
main()
{
    int i = 1; 								
    double sum =0;							
    clrscr();
    do								
    {
        sum = sum + 1.0 / (double)i;
        i++;
    } while(i<21);
    printf("sum=%lf\n",sum); 					
}


```
```
//5.4
#include<stdio.h>
main()
{
int i=15,sum=0;
while(i<15)
sum=sum+i;
printf("the sum is:%d",sum);
}


```
```
//5.5
#include<stdio.h>
main()
{
int i=15,sum=0;
do
{
sum=sum+i;
}while(i<15);
printf("the sum is:%d",sum);
}


```
```
//5.6
#include<stdio.h>
main()
{
int i,sum=0;
for(i=1;i<=100;i++)
sum=sum+i;
printf("the sum is %d:",sum);
}


```
```
//5.7
#include<stdio.h>
main()
{
int i=1,sum=0;
for(;i<=100;i++)
sum=sum+i;
printf("the sum is %d:",sum);
}


```
```
//5.8
#include<stdio.h>
main()
{
int i=1,sum=0;
for(;;i++)
{
if(i>100)
break;
sum=sum+i;
}
printf("the sum is %d:",sum);
}


```
```
//5.9
#include<stdio.h>
main()
{
int i=1,sum=0;
for(;;)
{
if(i>100)
break;
sum=sum+i;
i++;
}
printf("the sum is %d:",sum);
}


```
```
//5.10
#include<stdio.h>
main()
{
	int i=1,sum=0;
	for(;;)						
	{
		if(i>100)
			break; 						
		sum=sum+i;
		i++;
	}
	printf("the sum is %d:",sum);
}


```
```
//5.11
#include<stdio.h>
main()
{
int n=0;
printf("input a string\n");
loop: if(getchar()!='\n')
{ 
n++;
goto loop;
}
printf("%d",n);
}


```
```
//5.12
#include <stdio.h>
#include <math.h>
main()
{
    int a, b, c, d, flag = 0;
    scanf("%d", &a); 									
    for (b = 3; b <= a / 2; b += 2)								
    {
        for (c = 2; c <= sqrt(b); c++)								
		if (b % c == 0)
                break;
			if (c > sqrt(b))
            d = a - b;										
        else
            continue;
        for (c = 2; c <= sqrt(d); c++)								
            if (d % c == 0)
                break;
        if (c > sqrt(d))
        {
            printf("the result is:%d=%d+%d\n", a, b, d); 			
            flag = 1; 										
        }
    }
    if (flag == 0)
        printf("can not split!");
}


```
```
//5.13
#include<stdio.h>
main()
{
    int i, j, k; 							
    for (i = 1; i <= 5; i++)				
    {
        for (j = 1; j <= 5-i; j++)				
            printf(" ");
        for (k = 1; k <= 2 *i - 1; k++)			
            printf("#");
        printf("\n");
    }
}


```
```
//5.14
#include<stdio.h>
main()
{
    int i, j; 								
    for (i = 1; i <= 9; i++)						
    {
        for (j = 1; j <= i; j++)					
            printf("%d*%d=%d ", i, j, i *j);		
        printf("\n"); 						
    }
}


```
```
//5.15
#include <stdio.h>
main()
{
  int n=2,day=0;					
  float money=0,ave;				
  while(n<100)						
  {
    money+=0.8*n;					
    day++;						
    n*=2;							
  }
  ave=money/day;					
  printf("The result is %.6f",ave);
} 


```
```
//5.16
#include <stdio.h>
main()
{
    int cock, hen, chick;											
    for (cock = 0; cock <= 20; cock++)							
        for (hen = 0; hen <= 33; hen++)								
            for (chick = 3; chick <= 99; chick++)						
                if (5 *cock + 3 * hen + chick / 3 == 100) 				
                    if (cock + hen + chick == 100) 					
                        if (chick % 3 == 0) 							
                            printf("cock:%d hen:%d chick:%d\n", cock, hen,chick);
}


```
```
//5.17
#include <stdio.h>
main()
{
    int i, j, sum = 0;								
    for (i = 1; i < 1000; i++)							
    {
        sum = 0;
        for (j = 1; j < i; j++)
            if (i % j == 0) 						
                sum += j; 						
        if (sum == i) 							
            printf("%4d", i);
    }
}


```
```
//6.1
#include<stdio.h>
main()
{
    int a[5], i, temp; 									
    printf("please input array a:\n");
    for (i = 0; i < 5; i++)									
        scanf("%d", &a[i]);
    printf("array a:\n");
    for (i = 0; i < 5; i++)									
        printf("%d ", a[i]);
    printf("\n");
    for (i = 0; i < 2; i++)									
    {
        temp = a[i]; 									
        a[i] = a[4-i];
        a[4-i] = temp;
    }
    printf("Now array a:\n");
    for (i = 0; i < 5; i++)								
        printf("%d ", a[i]);
}


```
```
//6.2
#include<stdio.h>
main()
{
int i,a[8]={0,1,2,3,4,5,6,7};
for(i=0;i<8;i=i+2)
printf("%d\n",a[i]);
}


```
```
//6.3
#include<stdio.h>
main()
{
int i,a[8]={0,1,2,3};
for(i=0;i<8;i=i+2)
printf("%d\n",a[i]);
}


```
```
//6.4
#include<stdio.h>
main()
{
int i,a[]={0,1,2,3,4};
clrscr();
for(i=0;i<5;i=i+2)
printf("%d\n",a[i]);
}


```
```
//6.5
#include<stdio.h>
main()
{
int i,j,a[2][3]={{0,1,2},{3,4,5}};
for(i=0;i<2;i++)
{
for(j=0;j<3;j++)
printf("%5d",a[i][j]);
printf("\n");
}
}


```
```
//6.6
#include<stdio.h>
main()
{
int i,j,a[2][3]={5,4,3,2,1,0};
for(i=0;i<2;i++)
{
for(j=0;j<3;j++)
printf("%5d",a[i][j]);
printf("\n");
}
}


```
```
//6.7
#include<stdio.h>
main()
{
int i,j,a[2][3]={5,4,3};
for(i=0;i<2;i++)
{
for(j=0;j<3;j++)
printf("%5d",a[i][j]);
printf("\n");
}
}


```
```
//6.8
#include<stdio.h>
main()
{
int i,j,a[][3]={5,4,3,9,33,63};
for(i=0;i<2;i++)
{
for(j=0;j<3;j++)
printf("%5d",a[i][j]);
printf("\n");
}
}


```
```
//6.9
#include<stdio.h>
main()
{
    char a[5] =
    {
        '*', '*', '*', '*', '*'
    };										
    int i, j, k; 									
    for (i = 0; i < 5; i++)							
    {
        for (j = 1; j <= i; j++)					
            printf(" ");
        for (k = 0; k < 5; k++)
            printf("%c", a[k]);					
        printf("\n"); 						
    }
}


```
```
//6.10
#include<stdio.h>
main()
{
int i;
char array[12]={'h','e','l','l','o',' ','m','i','n','g','r','i'};
for(i=0;i<12;i++)
printf("%c",array[i]);
}


```
```
//6.11
#include<stdio.h>
main()
{
int i;
char array[12];
clrscr();
printf("please input string:\n");
for(i=0;i<12;i++)
scanf("%c",&array[i]);
printf("the string is:\n");
for(i=0;i<12;i++)
printf("%c",array[i]);
}


```
```
//6.12
#include<stdio.h>
main()
{
int i;
char array[22];
printf("please input string:\n");
scanf("%s",array);
printf("the string is:\n");
printf("%s",array);
}


```
```
//6.13
#include<stdio.h>
main()
{
int i;
char array1[10],array2[10],array3[10],array4[10];
printf("please input string:\n");
scanf("%s%s%s%s",array1,array2,array3,array4);
printf("the string is:\n");
printf("%s %s %s %s",array1,array2,array3,array4);
}

```
```
//6.14
#include<stdio.h>
#include<string.h>
main()
{
char c[]="hello\tkk\nhello\ttt";
puts(c);
}


```
```
//6.15
#include<stdio.h>
#include<string.h>
main()
{
char a[20];
printf("input string:\n");
gets(a);
puts(a);
}


```
```
//6.16
#include<stdio.h>
#include<string.h>
main()
{
    char a[100], b[100], c[200],  *p;
    int i = 0, j = 0, k = 0;
    printf("please input string a:\n");
    scanf("%s", a); 									
    printf("please input string b:\n");
    scanf("%s", b); 									
    while (a[i] != '\0' && b[j] != '\0')
    {
        if (a[i] < b[j])								
        {
            c[k] = a[i]; 								
            i++; 									
        }
        else
        {
            c[k] = b[j]; 								
            j++; 									
        }
        k++; 										
    }
    c[k] = '\0'; 										
    if (a[i] == '\0')								
        p = b + j;								
    else
        p = a + i;									
    strcat(c, p); 									
    puts(c); 									
}


```
```
//6.17
#include<stdio.h>
#include<string.h>
main()
{
char str1[30],str2[20];
printf("please input string1:\n");
gets(str1);
printf("please input string2:\n");
gets(str2);
strcpy(str1,str2);
printf("Now the string1 is:\n");
puts(str1);
}


```
```
//6.18
#include<stdio.h>
#include<string.h>
main()
{
char str1[30],str2[20];
clrscr();
printf("please input string1:\n");
gets(str1);
printf("please input string2:\n");
gets(str2);
strcat(str1,str2);
printf("Now the string1 is:\n");
puts(str1);
}


```

```
//6.19
#include<stdio.h>
#include<string.h>
main()
{
char str1[30],str2[20];
int i;
printf("please input string1:\n");
gets(str1);
printf("please input string2:\n");
gets(str2);
i=strcmp(str1,str2);
if(i>0)
printf("str1>str2\n");
else
if(i<0)
printf("str1<str2\n");
else
printf("str1=str2\n");
}


```
```
//6.20
#include<stdio.h>
#include<string.h>
main()
{
char str1[20],str2[20];
int len1,len2;
printf("please input string1:\n");
gets(str1);
printf("please input string2:\n");
gets(str2);
len1=strlen(str1);
len2=strlen(str2);
printf("the length of string1 is:%d\n",len1);
printf("the length of string2 is:%d\n",len2);
}


```
```
//6.21
#include<stdio.h>
#include<string.h>
main()
{
char str[20];
printf("please input string:\n");
gets(str);
strlwr(str);
printf("now the string is:\n");
puts(str);
}
```

```
//6.22
#include<stdio.h>
#include<string.h>
main()
{
char str[20];
printf("please input string:\n");
gets(str);
strupr(str);
printf("now the string is:\n");
puts(str);
}


```
```
//6.23
#include<stdio.h>
main()
{
    int i, v0 = 0, v1 = 0, v2 = 0, v3 = 0, n, a[50];
    printf("please input the number of electorate:\n");
    scanf("%d", &n); 											
    printf("please input 1or2or3\n");
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);										
    for (i = 0; i < n; i++)
    {
        if (a[i] == 1)
            v1++;													
        else if (a[i] == 2)
            v2++;												
        else if (a[i] == 3)
            v3++;											
        else
            v0++;													
    }
    printf("The Result:\n");
    printf("candidate1:%d\ncandidate2:%d\ncandidate3:%d\nnonuser:%d\n", v1, v2,
        v3, v0); 													
}


```
```
//6.24
#include <stdio.h>
main()
{
    int i, j, t, a[11];								
    printf("please input 10 numbers:\n");
    for (i = 1; i < 11; i++)
        scanf("%d", &a[i]);							
    for (i = 1; i < 10; i++)							
        for (j = 1; j < 11-i; j++)						
    if (a[j] > a[j + 1])
    {
        t = a[j];								
        a[j] = a[j + 1];
        a[j + 1] = t;
    }
    printf("the sorted numbers:\n");
    for (i = 1; i <= 10; i++)
        printf("%5d", a[i]);							
}


```
```
//6.25
#include<stdio.h>
main()
{
  int i,j,i1,j1,a[101][101],b[101][101];					
  printf("please input the number of rows(<=100)\n");		
  scanf("%d",&i1);							
  printf("please input the number of columns(<=100)\n");
  scanf("%d",&j1);								
  printf("please input the element\n");
  for(i=0;i<i1;i++)								
  for(j=0;j<j1;j++)								
  scanf("%d",&a[i][j]);								
  printf("array a:\n");								
  for(i=0;i<i1;i++)							
  {
    for(j=0;j<j1;j++)						
    printf("%d,",a[i][j]);						
    printf("\n");						
  }
  for(i=0;i<i1;i++)
  for(j=0;j<j1;j++)
  b[j][i]=a[i][j];								
  printf("array b:\n");							
  for(i=0;i<j1;i++)						
  {
    for(j=0;j<i1;j++)							
    printf("%d,",b[i][j]);						
    printf("\n");							
  }
}

```
```
//6.26
#include<stdio.h>
main()
{
  int i,j,x=1,y=3,a[6][6]={0};				
  for(i=1;i<=25;i++)
  {
    a[x][y] =i;							
    if(x==1&&y==5)
    {
      x=x+1;						
      continue;							
    }
    if(x==1)							
      x=5;
    else
      x--;								
    if(y==5)							
      y=1;
    else
      y++;						
    if(a[x][y]!=0)					
    {
      x=x+2;							
      y=y-1;
    }
  }
  for(i=1;i<=5;i++)						
  {
    for(j=1;j<=5;j++)
      printf("%4d",a[i][j]);
      printf("\n");						
  }
} 


```
```
//6.27
#include<stdio.h>
main()
{
    char c; 											
    int letters = 0, space = 0, digit = 0, others = 0;
        
    printf("please input some characters\n");
    while ((c = getchar()) != '\n')

    {
        if (c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z')
            letters++;							
        else if (c == ' ')
            space++;									
        else if (c >= '0' && c <= '9')
            digit++;								
        else
            others++;
         
    }
    printf("char=%d space=%d digit=%d others=%d\n", letters, space, digit,
        others);									
}


```
```
//6.28
#include<stdio.h>
main()
{
int i=0,j=0;					
printf("please input string1:\n");
scanf("%s",a);					
printf("please input string2:\n");
scanf("%s",b);				
while(a[i]!='\0')				
i++;
while(b[j]!='\0')					
a[i++]=b[j++];				
a[i]='\0';						
printf("%s",a);					


```

```
//7.1
int mul(int x,int y)
{
int z;
z=x*y;
return z;
}
main()
{
int a,b,c;
printf("please input a and b:\n");
scanf("%d,%d",&a,&b);
c=mul(a,b);
printf("the product is:%d",c);
}


```

```
//7.2
#include<stdio.h>
void show()
{
printf("***\n **\n  *\n");
}
main()
{
show();
}


```

```
//7.3
int ave(int a,int b)
{
int c;
c=(a+b)/2;
return c;
}
main()
{
int x,y,z;
printf("please input x,y:\n");
scanf("%d,%d",&x,&y);
z=ave(x,y);
printf("%d",ave(x,y));
ave(x,y);
}


```
```
//7.4
main()
{
int n;
printf("input number\n");
scanf("%d",&n);
f(n);
}
int f(int n)
{
int i;
if(n>0)
n=n+10;
else
if(n<0)
n=n+20;
else
n=100;
printf("n=%d\n",n);
}


```

```
//7.5
#include<stdio.h>
float average(float array[],int n)					
{
  int i;
  float aver,sum=0;
  for(i=0;i<n;i++)
  sum+=array[i];					
  aver=sum/n;								
  return(aver);								
}   
main()
{
  float height[100],aver;						
  int i,n;
  printf("please input the number of students:\n");
  scanf("%d",&n);							
  printf("please input student`s height:\n");
  for(i=0;i<n;i++)
  scanf("%f",&height[i]);							
  printf("\n");
  aver=average(height,n);							
  printf("average height is %6.2f",aver);				
}


```

```
//7.6
#include <stdio.h>
void insort(int s[], int n)							
{
    int i, j;
    for (i = 2; i <= n; i++)							
    {
        s[0] = s[i];								
        j = i - 1;								
        while (s[0] < s[j])
        {
            s[j + 1] = s[j];							
            j--;								
        }
        s[j + 1] = s[0];							
    }
}
main()
{
    int a[11], i;									
    printf("please input number:\n");
    for (i = 1; i <= 10; i++)
        scanf("%d", &a[i]);							
    printf("the original order:\n");
    for (i = 1; i < 11; i++)
        printf("%5d", a[i]);							
    insort(a, 10);									
    printf("\nthe sorted numbers:\n");
    for (i = 1; i < 11; i++)
        printf("%5d", a[i]);							
    printf("\n");
}


```
```
//7.7
#include<stdio.h>
void add(int x,int y)
{
int z;
z=x+y;
printf("%5d",z);
}
main()
{
int a[10],i;
printf("please input 10 numbers:\n");
for(i=0;i<10;i++)
scanf("%d",&a[i]);
printf("the result is:\n");
for(i=0;i<9;i++)
{
if(i%3==0)
printf("\n");
add(a[i],a[i+1]);
}
}


```

```
//7.8
int  cap(char c)
      { 
	if  (c>='A'&&c<='Z')
              return 1;
         else  
	      return 0;
      }
main()
      { 
	int i,num=0;
 	    char str[100];
	    printf("Input  a  string: ");
	    gets(str);
	    for(i=0;str[i]!='\0';i++)
	    if (cap(str[i]))
	      num++;
	    puts("the string is:");
	    puts(str);
	    printf("num=%d\n",num);
      }	


```

```
//7.9
#include<stdio.h>
main()
{
  int len;									
  char *str[100];							
  printf("please input a string:\n");
  gets(str);									
  len=length(str);						
  printf("the string has %d characters.",len);		
}
int length(char *p)							
{
  int n=0;									
  while(*p!='\0')							
  {
    n++;								
    p++;									
  }
  return n;									
}   


```
```
//7.10
#include<stdio.h>
main()
{
float average(float array[],int n);
  float height[100],aver;
  int i,n;
  printf("please input the number of students:\n");
  scanf("%d",&n);								
  printf("please input student`s height:\n");
  for(i=0;i<n;i++)
  scanf("%f",&height[i]);							
  printf("\n");
  aver=average(height,n);							
  printf("average height is %6.2f",aver);				
}
float average(float array[],int n)						
{
  int i;
  float aver,sum=0;
  for(i=0;i<n;i++)
  sum+=array[i];								
  aver=sum/n;								
  return(aver);								
}


```

```
//7.11
#include<stdio.h>
float add(float x,float y);
float sub(float x,float y);
float mul(float x,float y);
float div(float x,float y);
main()
{
float x,y;
printf("please input x and y:\n");
scanf("%f,%f",&x,&y);
printf("addition:%f\n",add(x,y));
printf("subtration:%f\n",sub(x,y));
printf("multiplication:%f\n",mul(x,y));
printf("division:%f\n",div(x,y));
}
float add(float x,float y)
{
float z;
z=x+y;
return z;
}
float sub(float x,float y)
{
float z;
if(x>y)
z=x-y;
else
z=y-x;
return z;
}
float mul(float x,float y)
{
float z;
z=x*y;
return z;
}
float div(float x,float y)
{
float z;
z=x/y;
return z;
}


```

```
//7.12
#include<stdio.h>
int gys(int x,int y)							
{
  return y?gys(y,x%y):x;					
}
int gbs(int x,int y)							
{
  return x/gys(x,y)*y;
}
void yuefen(int fz,int fm)					
{ 
  int s=gys(fz,fm);
  fz/=s;
  fm/=s;
  printf("the result is %d/%d\n",fz,fm);
}
void add(int a,int b,int c,int d)					
{
  int u1,u2,v,fz1,fm1;
  v=gbs(b,d);
  u1=v/b*a;
  u2=v/d*c;
  fz1=u1+u2;
  fm1=v;
  yuefen(fz1,fm1);
}
main()
{ 
  int a,b,c,d;
  scanf("%ld,%ld,%ld,%ld",&a,&b,&c,&d);
  add(a,b,c,d);							
}


```
```
//7.13
#include<stdio.h>
int age(int n)										
{
  int f;
  if(n==1)						
  f=10;												
  else
  f=age(n-1)+2;										
  return f;											
}
main()
{
  int i,j;												
  printf("Do you want to know whose age?please input:\n");
  scanf("%d",&i);										
  j=age(i);											
  printf("the age is %d",j);								
} 


```

```
//7.14
#include<stdio.h>
main()
{
int n,value;
printf("please input n:\n");
scanf("%d",&n);
value=factor1(n);
printf("%d factorial is:%d",n,value);
}
int factor1(int n)
{
int result;
if(n==1)
return 1;
result=factor1(n-1)*n;
return result;
}


```

```
//7.15
#include<stdio.h>
int min=10000,max=0;
void change(int a[],int n)
{
    int i,j,k;
    for (i = 0; i < n; i++)								
    if (a[i] < min)
    {
        min = a[i];
        j = i; 										
    }
    for (i = 0; i < n; i++)								
    if (a[i] > max)
    {
        max = a[i];
        k = i; 										
    }
    a[k] = min; 										
    a[j] = max; 										
    printf("\nthe position of min is:%3d\n", j);			
    printf("the position of max is:%3d\n", k);					
    printf("Now the array is:\n");
    for (i = 0; i < n; i++)
        printf("%5d", a[i]);
	}
main()
{
    int a[20], i, n; 										
    printf("please input the nunber of elements:\n");
    scanf("%d", &n); 									
    printf("please input the element:\n");
    for (i = 0; i < n; i++)								
        scanf("%d", &a[i]);
    change(a,n);
    printf("\nmax=%5d\nmin=%5d",max,min);
}


```
```
//7.16
#include<stdio.h>
main()
{
auto int i,j,k;
printf("please input the number:\n");
scanf("%d,%d",&i,&j);
if(i!=0&&j!=0)
if(i>j)
k=i-j;
else
k=i+j;
printf("the resullt is %d\n",k);
}


```

```
//7.17
#include<stdio.h>
main()
{
auto int i,j,k;
printf("please input the number:\n");
scanf("%d,%d",&i,&j);
k=i*i+j*j;
if(i!=0&&j!=0)
{
auto int k;
if(i>j)
k=i-j;
else
k=i+j;
printf("result1 is%d\n",k);
}
printf("result2 is %d\n",k);
}


```

```
//7.18
#include<stdio.h>
int add(int x)
{
static int n=0;
n=n+x;
return n;
}
main()
{
int i,j,sum;
printf("please input the number:\n");
scanf("%d",&i);
printf("the result is:\n");
for(j=1;j<=i;j++)
{sum=add(j);
printf("%d: %d\n",j,sum);
}
}


```
```
//7.19
#include<stdio.h>
main()
{
register i,s=0;
for(i=1;i<=100;i++)
s=s+i;
printf("s=%d\n",s);
}


```

```
//7.20
#include<stdio.h>
main()
{
extern int X,Y;
printf("this is an example!\n");
printf("the extern variable is %d,%d",X,Y);
}
int X=96,Y=88;


```

```
//7.21
#include <stdio.h>
#include <math.h>
main()
{
    int i;												
    printf("please input a number:\n");						
    scanf("%d", &i);										
    printf("number: %d ,absolute value: %d ", i, abs(i));		
}

```

```
//7.22
#include <ctype.h>
#include <stdio.h>
main()
{
    char ch, ch1;
    while (1)
    {
        printf("input the character('q' to quit):");
        ch = getchar(); 									
        ch1 = getchar(); 									
        if (ch == 'q' || ch == 'Q')								
            break;										
        if (isalpha(ch))									
            printf("\n%c is a letter.\n\n", ch);
        else
            printf("\n%c is not a letter.\n\n", ch);
    }
}

```

```
//7.23
#include <stdio.h>
int leap(int a)										
{
    if (a % 4 == 0 && a % 100 != 0 || a % 400 == 0)		
        return 1;								
    else
        return 0;									
}
int number(int year, int m, int d) 							
{
    int sum = 0, i, j, k, a[12] =
    {
        31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    };									
    int b[12] =
    {
        31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    };									
    if (leap(year) == 1)								
        for (i = 0; i < m - 1; i++)
            sum += b[i];							
    else
        for (i = 0; i < m - 1; i++)
            sum += a[i];							
    sum += d;									
    return sum;									
}
main()
{
    int year, month, day, n;								
    printf("please input year,month,day\n");
    scanf("%d%d%d", &year, &month, &day);			
    n = number(year, month, day);							
    printf("di %d tian\n", n);
}

```

```
//7.24
#include <stdio.h>
int difference(int a[])						
{
    int t, i, j, sum, sum1, sum2;
    for (i = 0; i < 3; i++)						
        for (j = i + 1; j < 4; j++)
    if (a[i] < a[j])
    {
        t = a[i];
        a[i] = a[j];
        a[j] = t;
    }
    sum1 = a[0] *1000+a[1] *100+a[2] *10+a[3];		
    sum2 = a[3] *1000+a[2] *100+a[1] *10+a[0];		
    sum = sum1 - sum2;						
    printf("%5d=%5d-%5d\n", sum, sum1, sum2); 			
    return sum;						
}
main()
{
    int i, j, k, l, n, a[4];
    printf("please input a number:\n");
    scanf("%d", &n);							
    while (n != 6174)
    {
        a[0] = n / 1000;						
        a[1] = n / 100 % 10;						
        a[2] = n / 10 % 10;							
        a[3] = n % 10;							
        n = difference(a);						
    }
}
```


