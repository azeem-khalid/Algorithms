#include<stdio.h>
#include<conio.h>
void Dijkstras(int nodes,int vertices,int weight[10][10],int path[])
{
int u,count,flag[10],min;
for(int i=1;i<=nodes;i++)
flag[i]=0,path[i]=weight[vertices][i];
count=2;
while(count<=nodes)
{
min=99;
for(int i=1;i<=nodes;i++)
if(path[i]<min && !flag[i])
min=path[i],u=i;
flag[u]=1;
count++;
for(int z=1;z<=nodes;z++)
if((path[u]+weight[u][z]<path[z]) && !flag[z])
path[z]=path[u]+weight[u][z];
}
}
int main()
{
int nodes,vertices,weight[10][10],path[10];
printf("\t Creating Graph!!!\n");
printf("\nEnter the number of nodes: ");
scanf("%d",&nodes);
printf("\nEnter the weight matrix: \n");
for(int x=1;x<=nodes;x++){
for(int y=1;y<=nodes;y++)
{
scanf("%d",&weight[x][y]);
if(weight[x][y]==0)
weight[x][y]=999;
}}
printf("\nEnter the source matrix: ");
scanf("%d",&vertices);
Dijkstras(nodes,vertices,weight,path);
printf("\t Result!!!\n");
printf("\nShortest path: ");
for(int x=1;x<=nodes;x++)
if(x!=vertices)
printf("\n%d->%d,weight=%d\n",vertices,x,path[x]);
getch();
}
