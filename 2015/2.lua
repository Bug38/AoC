function readAll(file)
  local f = assert(io.open(file, "rb"))
  local content = {}
  while true do
    line = f:read()
    if not line then break end
    table.insert(content,line)
  end
  f:close()
  return content
end

local input = readAll("input2.txt")

--input = {
--  "2x3x4",
--  "1x1x10"
--}

local paperSize = 0
local ribbonSize = 0

for i=1,#input do
  local l, w, h = input[i]:match("(%d+)x(%d+)x(%d+)")
  local s1, s2, s3 = l*w, w*h, h*l
  paperSize = paperSize + 2*s1 + 2*s2 + 2*s3 + math.min(s1, s2, s3)
  ribbonSize = ribbonSize + 2*(l+w+h-math.max(l,w,h)) + l*w*h
end

print("Elves need "..paperSize.." square feet of paper and "..ribbonSize.." feet of ribbon.")