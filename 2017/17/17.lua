function readAll(file)
  local f = assert(io.open(file, "rb"))
  local content = {}
  while true do
    line = f:read()
    if not line then
      break
    end
    table.insert(content, line)
  end
  f:close()
  return content
end

local input = readAll("input17.txt")


--input = { 'snd 1',
--  'snd 2',
--  'snd p',
--  'rcv a',
--  'rcv b',
--  'rcv c',
--  'rcv d',
--}

local vars = {
  prog0 = {
    p = 0,
    timesSent = 0,
    isWaiting = false,
  },
  prog1 = {
    p = 1,
    timesSent = 0,
    isWaiting = false,
  }
}

local i = {
  prog0 = 1,
  prog1 = 1
}

local sent = {
  prog0 = {},
  prog1 = {}
}

local function iter(prog, other)
  print(input[i[prog]])
  --local out = prog..' : '
  if vars[prog].isWaiting == true then
    return
  end
  local instr = input[i[prog]]:match("(%a%a%a).*")
  local op1, op2 = "", ""
  if instr == "set" then
    op1, op2 = input[i[prog]]:match("%a+ (%a+) ([-%a%d]+)")
    vars[prog][op1] = tonumber(op2) or vars[prog][op2]
    --out = out .. "set "
  elseif instr == "add" then
    op1, op2 = input[i[prog]]:match("%a+ (%a+) ([-%a%d]+)")
    vars[prog][op1] = (vars[prog][op1] or 0) + (tonumber(op2) or vars[prog][op2])
  elseif instr == "mul" then
    op1, op2 = input[i[prog]]:match("%a+ (%a+) ([-%a%d]+)")
    vars[prog][op1] = (vars[prog][op1] or 0) * (tonumber(op2) or vars[prog][op2])
  elseif instr == "mod" then
    op1, op2 = input[i[prog]]:match("%a+ (%a+) ([-%a%d]+)")
    vars[prog][op1] = (vars[prog][op1] or 0) % (tonumber(op2) or vars[prog][op2])
  elseif instr == "snd" then
    --print(prog .. " : " .. input[i[prog]])
    op1 = input[i[prog]]:match("%a+ ([%a%d]+)")
    table.insert(sent[prog], #sent[prog] + 1, vars[prog][op1] or 0)
    vars[prog].timesSent = vars[prog].timesSent + 1
    --print("\tIn sent_"..prog.." : "..#sent[prog])
    vars[other].isWaiting = false
  elseif instr == "rcv" then
    --print(prog .. " : " .. input[i[prog]])
    op1 = input[i[prog]]:match("%a+ (%a+)")
    if #sent[other] > 0 then
      vars[prog][op1] = table.remove(sent[other], 1)
      --print(prog.." recovered value")
      --print(prog.." no longer waits")
    else
      vars[prog].isWaiting = true
      --print(prog.." is waiting")
      i[prog] = i[prog] - 1
    end
  elseif instr == "jgz" then
    op1, op2 = input[i[prog]]:match("%a+ ([%a%d]+) ([-%a%d]+)")
    if (tonumber(op1) or vars[prog][op1]) > 0 then
      i[prog] = (i[prog] + (tonumber(op2) or vars[prog][op2])) - 1
    end
  else
    print("Instruction inconnue : " .. instr)
  end
  i[prog] = i[prog] + 1
  --print(i[prog])
end

while not (vars["prog0"].isWaiting and vars["prog1"].isWaiting) do
  iter("prog0", "prog1")
  iter("prog1", "prog0")
end

print("prog0 sent " .. vars["prog0"].timesSent .. " times")
print("prog1 sent " .. vars["prog1"].timesSent .. " times")