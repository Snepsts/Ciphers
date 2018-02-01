/*
Jonathon Bryant
This program encrypts a message using the autokey cipher.
*/

using System;
using System.Collections.Generic;

namespace AutoKey{
  class Cipher{
    public static void Main(){
      Dictionary<string, int> dict = new Dictionary<string, int>();
      dict.Add("a", 0);
      dict.Add("b", 1);
      dict.Add("c", 2);
      dict.Add("d", 3);
      dict.Add("e", 4);
      dict.Add("f", 5);
      dict.Add("g", 6);
      dict.Add("h", 7);
      dict.Add("i", 8);
      dict.Add("j", 9);
      dict.Add("k", 10);
      dict.Add("l", 11);
      dict.Add("m", 12);
      dict.Add("n", 13);
      dict.Add("o", 14);
      dict.Add("p", 15);
      dict.Add("q", 16);
      dict.Add("r", 17);
      dict.Add("s", 18);
      dict.Add("t", 19);
      dict.Add("u", 20);
      dict.Add("v", 21);
      dict.Add("w", 22);
      dict.Add("x", 23);
      dict.Add("y", 24);
      dict.Add("z", 25);

      string CipherText = "";
      string sentence = Console.ReadLine();
      sentence = sentence.ToLower();
      int length = sentence.Length;
      string key = Console.ReadLine();
      key = key.ToLower();
      List<int> cList = new List<int>();
      List<int> lList = new List<int>();

      for(int i = 0; i < key.Length; i++){
        foreach(KeyValuePair<string, int> x in dict){
          if(x.Key == key[i].ToString()){
            cList.Add(x.Value);
          }
        }
      }

      for(int i = 0; cList.Count < length; i++){
        foreach(KeyValuePair<string, int> x in dict){
          if(x.Key == sentence[i].ToString()){
            cList.Add(x.Value);
          }
        }
      }

      for(int i = 0; i < cList.Count; i++){
        foreach(KeyValuePair<string, int> x in dict){
          if(x.Key == sentence[i].ToString()){
            lList.Add((x.Value + cList[i]) % 26);
          }
        }
      }

      for(int i = 0; i < lList.Count; i++){
        foreach(KeyValuePair<string, int> x in dict){
          if(x.Value == lList[i]){
            CipherText += x.Key.ToUpper();
          }
        }
      }

      for(int i = 0; i < CipherText.Length; i++){
        if((i % 5) == 0 && i != 0){
          Console.Write(" ");
        }
        if((i % 50) == 0 && i != 0){
          Console.WriteLine("");
        }
        Console.Write(CipherText[i]);
      }
      Console.WriteLine("");

    }
  }
}
