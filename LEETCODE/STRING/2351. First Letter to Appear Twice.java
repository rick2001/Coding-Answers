//java sollution
class Solution {
    public char repeatedCharacter(String s) {
        char[] charArray=s.toCharArray();
        List<Character> array=new ArrayList<>();
        char result='a'; //assigining dummy value;
        for(int i=0; i<charArray.length; i++){
            if(array.contains(charArray[i])){
                result=charArray[i];
                break;
            }
            else{
                array.add(charArray[i]);
            }
        }
        return result;
    }
}


// python solution
class Solution(object):
    def repeatedCharacter(self, s):
        hashmap={}
        for val in s:
            if val in hashmap:
                hashmap[val]+=1
            else:
                hashmap[val]=1
            if hashmap[val]==2:
                return val
                
