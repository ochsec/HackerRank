// https://www.hackerrank.com/challenges/find-point

using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    static void Main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution */
        int n = Convert.ToInt32(System.Console.ReadLine());
        double[][] a = new double[n][];
        for(int a_i = 0; a_i < n; a_i++){
           string[] a_temp = Console.ReadLine().Split(' ');
           a[a_i] = Array.ConvertAll(a_temp,Double.Parse);
        }
        
        for (int i = 0; i < a.Length; i++)
        {
            double[] newCoords = translateToOrigin(a[i]); 
            double[] reflectedCoords = new double[4];            
            reflectedCoords[0] = -newCoords[0];
            reflectedCoords[1] = -newCoords[1];
            reflectedCoords[2] = a[i][2];
            reflectedCoords[3] = a[i][3];
            double[] finalCoords = translateBack(reflectedCoords);
            
            System.Console.WriteLine($"{finalCoords[0]} {finalCoords[1]}");
        }
    }
    
    static double[] translateToOrigin(double[] coords) 
    {
        double[] newCoords = new double[4];
        double x1 = coords[2];
        double y1 = coords[3];
        double x2 = coords[0];
        double y2 = coords[1];
        
        newCoords[0] = x2 - x1;
        newCoords[1] = y2 - y1;
        return newCoords;
    }
    
    static double[] translateBack(double[] coords)
    {
        double[] newCoords = new double[2];
        double x1 = coords[2];
        double y1 = coords[3];
        double x2 = coords[0];
        double y2 = coords[1];
        
        newCoords[0] = x1 + x2;
        newCoords[1] = y1 + y2;
        return newCoords;
    }
}