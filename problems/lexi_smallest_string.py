
class Lexi:

    def dfs(self, src):

        self.visited[src] = 1

        self.minChar = min(src, self.minChar)

        self.node_list.append(src)

        for i in range(26):
            if self.graph_mat[src][i] and (self.visited[i]==0):
                self.dfs(i)

    def lexis(self, str1, str2, base_str):

        self.graph_mat = [[0 for i in range(26)] for i in range(26)]
        
        for i in range(len(str1)):
            self.graph_mat[(ord(str1[i])%32)-1][(ord(str2[i])%32)-1] = 1
            self.graph_mat[(ord(str2[i])%32)-1][(ord(str1[i])%32)-1] = 1

        mappingChar = [1]*26
        self.visited = [0]*26

        for  i in range(26):

            if not self.visited[i]:
                
                self.node_list = []
                self.minChar = 27
                self.dfs(i)

                for n in self.node_list:
                    mappingChar[n] = self.minChar
                
                print(mappingChar)
        
        final_str = ""
        for s in base_str:
            num_s = ord(s)%32
            final_str = final_str + (chr(96+mappingChar[num_s-1]+1))
        print(final_str)


ste1 = 'leetcode'
ste2 = 'programs'
base_str = "sourcecode"
l = Lexi()
l.lexis(ste1, ste2, base_str)

