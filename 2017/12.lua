function readAll(file)
  local f = assert(io.open(file, "rb"))
  local content = f:read("*all")
  f:close()
  return content
end

local input = readAll("input12.txt")

--input = [[0 <-> 2
--1 <-> 1
--2 <-> 0, 3, 4
--3 <-> 2, 4
--4 <-> 2, 3, 6
--5 <-> 6
--6 <-> 4, 5]]

--------------------------
----- DAY 11 -------------
--------------------------

local programs = {}
local nbProg = 0

local inGroup = {}

-- populate programs
for line in input:gmatch("[^\n.]*") do
  if #line > 0 then
    local prog, childs = line:match("(%d+) <%-> ([%d, ]+)")
    programs[prog] = {}
    for child in childs:gmatch("%d+") do
      table.insert(programs[prog], child)
      nbProg = nbProg + 1
    end
  end
end

local nbGroups = 0

function addChilds(prog)
  print("Add child "..tostring(prog))
  print(" -> "..#programs[tostring(prog)].." children")
  if #programs[prog] > 0 then
    for i,j in pairs(programs[prog]) do --for each child
      print("Processing child "..i.." : "..j)
      local isInGroup = false
      for i=1,#inGroup do
        if inGroup[i] == j then isInGroup = true break end
      end
      if not isInGroup then
        table.insert(inGroup,j)
        addChilds(j)
        print("Remove child "..j.." from programs list")
        programs[j] = nil
      end
    end
  end
end

local prog = 0
while nbProg > 0 do
  if programs[tostring(prog)] then
    addChilds(tostring(prog))
    nbGroups = nbGroups + 1
  end
  prog = prog + 1
  nbProg = nbProg - 1
end

--print("In group : "..#inGroup)
print("Groups : "..nbGroups)