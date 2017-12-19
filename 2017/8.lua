function readAll(file)
  local f = assert(io.open(file, "rb"))
  local content = f:read("*all")
  f:close()
  return content
end

local input = readAll("input8.txt")

--input = [[
--b inc 5 if a > 1
--a inc 1 if b < 5
--c dec -10 if a >= 1
--c inc -20 if c == 10
--]]

--------------------------
----- DAY 8 --------------
--------------------------

input = input:gsub("!=","~=")
input = input:gsub("inc","+")
input = input:gsub("dec","-")

input = input:gsub("(%a+) ([%+%-]) ([%-]*%d+) if (%a+) ([<>=~]+ [%-]*%d+)", [[vars.%1 = ((vars.%4 or 0) %5) and ((vars.%1 or 0) %2 %3) or (vars.%1 or 0)
if (vars.%1 > top) then top = vars.%1 end
]])

input = [[
local vars = {}
local top  = 0
]]..input..[[
return vars, top
]]

--print(input)

local func = loadstring(input)
local vars, top = func()
local numbers = {}

for i,j in pairs(vars) do
  table.insert(numbers,j)
end

print("max value (end) : "..math.max(unpack(numbers)))
print("max value (reached) : "..top)