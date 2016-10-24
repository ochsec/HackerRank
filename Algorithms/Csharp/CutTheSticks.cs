// https://www.hackerrank.com/challenges/cut-the-sticks

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution {

    static void Main(String[] args) {
        int n = Convert.ToInt32(Console.ReadLine());
        string[] arr_temp = Console.ReadLine().Split(' ');
        int[] arr = Array.ConvertAll(arr_temp,Int32.Parse);
        
        int count = 0;
        int pos = 0;
        int remaining = n;
        Array.Sort(arr);

        System.Console.WriteLine(n);
        while (remaining > 0)
        {
            if (arr[pos] <= 0)
            {
                pos++;
                continue;
            }
            int amount = arr[pos];
            for (int i = 0; i < arr.Length; i++)
            {
                arr[i] = arr[i] - amount;
                if (arr[i] > 0) count++;
            }
            remaining = count;
            if(remaining > 0) System.Console.WriteLine(count);
            count = 0;
        }
    }
}
