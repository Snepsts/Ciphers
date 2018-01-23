/*
Author: Jonathon Bryant

Description: This is a C# program that encrypts a message using Substitution
cipher.
*/

using System;
using System.Collections.Generic;

namespace SubstitutionCipher{
  class Substitution{
    public static void Main(){
      string CipherText = "";
      Dictionary<string, string> dict = new Dictionary<string, string>();
        dict.Add("a", "X");
        dict.Add("b", "N");
        dict.Add("c", "Y");
        dict.Add("d", "A");
        dict.Add("e", "H");
        dict.Add("f", "P");
        dict.Add("g", "O");
        dict.Add("h", "G");
        dict.Add("i", "Z");
        dict.Add("j", "Q");
        dict.Add("k", "W");
        dict.Add("l", "B");
        dict.Add("m", "T");
        dict.Add("n", "S");
        dict.Add("o", "F");
        dict.Add("p", "L");
        dict.Add("q", "R");
        dict.Add("r", "C");
        dict.Add("s", "V");
        dict.Add("t", "M");
        dict.Add("u", "U");
        dict.Add("v", "E");
        dict.Add("w", "K");
        dict.Add("x", "J");
        dict.Add("y", "D");
        dict.Add("z", "I");

      string sentence = Console.ReadLine();
      sentence = sentence.ToLower();
      int length = sentence.Length;

      for(int i = 0; i < length; i++){
          foreach(KeyValuePair<string,string> x in dict){
            if(x.Key == sentence[i].ToString()){
              CipherText = CipherText + x.Value;
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
