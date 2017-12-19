local input = "ckczppom"

--input = "abcdef"

local expected = "000000"

local md5 = require 'md5'
for i=0, 1000000000 do
  if md5.sumhexa(input..i):sub(1,#expected) == expected then
    print(i)
    print(md5.sumhexa(input..i))
    break
  end
end
