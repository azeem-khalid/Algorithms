/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package dfs;
import java.io.*;
import java.util.*;
/**
 *
 * @author Dell
 */
class Graphs
{
    public
    int V;
    LinkedList list[];
    Graphs(int vertex)
    {
        V = vertex;
        list = new LinkedList[vertex];
        for (int i=0; i<vertex;i++)
        list[i] = new LinkedList();
    }
    
    public void add(int vertex, int edge)
    {
        list[vertex].add(edge);
    }
    public void continue1(int set,boolean visited[])
    {
        visited[set] = true;
        System.out.print(set +" ");
        Iterator<Integer> i = list[set].listIterator();
        while (i.hasNext())
        {
            int n = i.next();
            if (!visited[n])
            continue1(n, visited);
        }
    }

    public void DepthFirstTraversal(int v)
    {
        boolean visited[] = new boolean[V];
        continue1(v, visited);
    }
}

public class DFS {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
 Graphs g = new Graphs(4);
 g.add(0, 1);
 g.add(0, 2);
 g.add(1, 2);
 g.add(2, 0);
 g.add(2, 3);
 g.add(3, 3);
 System.out.println("Depth First Traversal ");
 g.DepthFirstTraversal(2);
    }
    
}