--function readAll(file)
--  local f = assert(io.open(file, "rb"))
--  local content = {}
--  while true do
--    line = f:read()
--    if not line then
--      break
--    end
--    table.insert(content, line)
--  end
--  f:close()
--  return content
--end
--
--local input = readAll("input5.txt")
--local niceStrings = 0
--
--local disallowed = { "ab","cd","pq","xy" }
--local vowels = { "a","e","i","o","u" }
--
--input = { "qjhvhtzxzqqjkmpb" }
--
--for line in io.lines("input5.txt") do
--  testA,testB = false, false
--
--  line = input[1]
--
--  for i=1,#line -2 do
--    if line:sub(i,i) == line:sub(i+2,i+2) then testA = true break end
--  end
--
--  for i=1,#line-1 do
--    sub1 = line:sub(i,i+1)
--    for j=2,#line do
--      if (j < i - 1) or (j > i + 3) then
--        if sub1 == line:sub(j-1,j) then
--          testB = true end
--      end
--    end
--  end
--
--  if testA and testB then
--    niceStrings = niceStrings + 1
--  end
--break
--end
--
--print(niceStrings)



niceStrings = 0

for line in io.lines("input5.txt") do
  paramA, paramB = false, false

  for i = 1, #line - 2 do
    c = line:sub(i,i)
    c3 = line:sub(i + 2, i + 2)

    if c == c3 then
      paramB = true
      break
    end
  end

  for i = 1, #line - 1 do
    local c = line:sub(i, i + 1)
    for x = 1, #line do
      if x ~= i and x ~= i + 1 and x ~= i - 1 then
        if c == line:sub(x, x + 1) then
          paramA = true
          break
        end
      end
    end
  end

  if paramA and paramB then
    niceStrings = niceStrings + 1;
  end
end
print(niceStrings)














