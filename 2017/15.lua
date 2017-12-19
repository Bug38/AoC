local inputA = 618
local inputB = 814

--inputA = 65
--inputB = 8921

local coefA  = 16807
local coefB  = 48271

local divider= 2147483647

local floor,insert = math.floor, table.insert
function base2(n)
  n = floor(n)
  local out = ""
  for i=1,16 do
    out = n%2 .. out
    n = floor(n / 2)
  end
  return out
end

local total = 0

for i=1,5000000 do
  --print(base2(inputA).."\t"..base2(inputB))
  repeat
    inputA = (inputA*coefA)%divider
  until inputA%4 == 0
  repeat
    inputB = (inputB*coefB)%divider
  until inputB%8 == 0
  if bit.band(inputA,0xFFFF) == bit.band(inputB,0xFFFF) then
  --if base2(inputA) == base2(inputB) then
    total = total + 1 end
  if i%1000000 == 0 then print(i) end
end

print(total)