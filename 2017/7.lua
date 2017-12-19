function readAll(file)
  local f = assert(io.open(file, "rb"))
  local content = f:read("*all")
  f:close()
  return content
end

local input = readAll("input7.txt")

--input = [[pbga (66)
--xhth (57)
--ebii (61)
--havc (66)
--ktlj (57)
--fwft (72) -> ktlj, cntj, xhth
--qoyq (66)
--padx (45) -> pbga, havc, qoyq
--tknk (41) -> ugml, padx, fwft
--jptl (61)
--ugml (68) -> gyxo, ebii, jptl
--gyxo (61)
--cntj (57)]]

function string:split(sep)
  local sep, fields = sep or "\n", {}
  local pattern = string.format("([^%s]+)", sep)
  self:gsub(pattern, function(c)
    fields[#fields + 1] = c
  end)
  return fields
end

function parseNodes(str)
  local n, v, ch
  n = str:match("^[a-z]+")
  d = str:match("[0-9]+")
  ch = str:match("[a-z ,]+$")
  if ch then
    ch, _ = ch:gsub(" ", "")
    ch = ch:split(",")
  end
  return n, d, ch
end

function repeats(s, n)
  return n > 0 and s .. repeats(s, n - 1) or ""
end

function printNode(node, offset)
  offset = offset or 0
  print(repeats("  ", offset) .. node.name .. " (" .. node.value .. ")")
  if node.children then
    for _, ch in pairs(node.children) do
      if node.children[ch] then printNode(node.children[ch], offset+1) end
    end
  end
end

function treeWeight(node)
  local weight = 0
  if node.children then
    local childrenWeights = {}
    for _, ch in pairs(node.children) do
      if node.children[ch] then
        local chWeight = treeWeight(node.children[ch])
        childrenWeights[ch] = chWeight
        weight = weight + chWeight
      end
    end
    local isOK = true
    for i,j in pairs(childrenWeights) do
      if childrenWeights[i] ~= weight/#node.children then isOK = false break end
    end
    if isOK == false then
      print("Unbalanced node : "..node.name)
      for i,j in pairs(childrenWeights) do
        print(i,j)
      end
    end
  end

  return weight + node.value
end

local tmpNodes = input:split("\n")
local nodes = {}
local top = ""

local function isParent(node, table)
  for i, ch in ipairs(node.children) do
    if ch == table.name then
      return ch
    end
  end
end

for i = 1, #tmpNodes do
  local n, v, ch = parseNodes(tmpNodes[i])
  nodes[n] = {
    name = n,
    value = v,
    children = {}
  }
  nodes[n].children = ch
  last = n
end

function finduniq(txt)
  local allNodes = {}
  for word in txt:gmatch("%a+") do
    table.insert(allNodes,word)
  end
  table.sort(allNodes,function(a,b) return a<b end)
  local i = 1
  while #allNodes > 1 do
    if allNodes[i] == allNodes[i+1] then
      table.remove(allNodes,i)
      table.remove(allNodes,i)
      i=i-1
    end
    i = i+1
  end
  return allNodes[1]
end

top = nodes[finduniq(input)]
--print("top node : "..top.name)

function appendChilds(node)
  for i=1, #node.children do
    --print("appending child "..node.children[i])
    node.children[node.children[i]] = nodes[node.children[i]]
    if node.children[node.children[i]].children then appendChilds(node.children[node.children[i]]) end
  end
end

function createTree(n)
  if n.children then appendChilds(n) end
end

createTree(top)

function checkBalance(node)
  for i,j in pairs(top.children) do
    if type(i) == "string" then
      print(treeWeight(j))
    end
  end
end

--printNode(top)
--checkBalance(top)
treeWeight(top)

printNode(nodes["jriph"])