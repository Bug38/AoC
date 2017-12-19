local input = 347991

--local input = 26

--[[
  Part 1
]]--

--local tmp = math.floor(math.sqrt(input))
--local s = tmp%2==0 and tmp+1 or tmp%2==1 and tmp+2
--
--local br,bl,tl,tr = s*s,s*s-(s-1),s*s-2*(s-1),s*s-3*(s-1)
--local b,l,t,r = br-math.floor(s/2),bl-math.floor(s/2),tl-math.floor(s/2),tr-math.floor(s/2)
--
--local dist = 0
--
--if input > bl then
--  dist = math.abs(b-input) + math.floor(s/2)
--elseif input > tl then
--  dist = math.abs(l-input) + math.floor(s/2)
--elseif input > tr then
--  dist = math.abs(t-input) + math.floor(s/2)
--else
--  dist = math.abs(r-input) + math.floor(s/2)
--end
--
--print("s : "..s)
--print("dist : "..dist)

--[[
  Part 2
]]--

local tmp = math.floor(math.sqrt(input))
local s = tmp%2==0 and tmp+1 or tmp%2==1 and tmp+2

local br,bl,tl,tr = s*s,s*s-(s-1),s*s-2*(s-1),s*s-3*(s-1)
local b,l,t,r = br-math.floor(s/2),bl-math.floor(s/2),tl-math.floor(s/2),tr-math.floor(s/2)

local dist = 0

if input > bl then
  dist = math.abs(b-input) + math.floor(s/2)
elseif input > tl then
  dist = math.abs(l-input) + math.floor(s/2)
elseif input > tr then
  dist = math.abs(t-input) + math.floor(s/2)
else
  dist = math.abs(r-input) + math.floor(s/2)
end

print("s : "..s)
print("dist : "..dist)

