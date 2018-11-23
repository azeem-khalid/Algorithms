#include<stdio.h>
#include<conio.h>
int main()
{
int var1,var2,vertices,nodes,x,y,z,ne=1;
int visited[10]={0},weight[10][10];
int Minim,minimWeight=0;
printf("\t Creating Graph!!!\n");
printf("\nEnter the number of nodes: ");
scanf("%d",&nodes);
printf("\nEnter the adjacency matrix: \n");
for(int x=1;x<=nodes;x++)
for(int y=1;y<=nodes;y++)
{
scanf("%d",&weight[x][y]);
if(weight[x][y]==0)
weight[x][y]=999;
}
visited[1]=1;
printf("\n");
while(ne<nodes)
{
for(int x=1,Minim=999;x<=nodes;x++)
for(int y=1;y<=nodes;y++)
if(weight[x][y]<Minim)
if(visited[x]!=0)
{
Minim=weight[x][y];
var1=z=x;
var2=vertices=y;
}
if(visited[z]==0 || visited[vertices]==0)
{
printf("\nEdge %d: ( %d , %d ) weight:%d",ne++,var1,var2,Minim);
minimWeight+=Minim;
visited[var2]=1;
}
weight[var1][var2]=weight[var2][var1]=999;
}
printf("\t Result!!!\n");
printf("\nMinimum Weight=%d",minimWeight);
getch();
}
