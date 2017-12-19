function readAll(file)
  local f = assert(io.open(file, "rb"))
  local content = f:read("*all")
  f:close()
  return content
end

local input = readAll("input1.txt")

local lvl = 0

local evol = {
  ['('] =  1,
  [')'] = -1
}

for i=1,#input do
  lvl = lvl + evol[input:sub(i,i)]
  if lvl == -1 then print("Level -1 at step : "..i) end
end

print("Final level : "..lvl)