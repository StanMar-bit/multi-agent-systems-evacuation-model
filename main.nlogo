__includes [
  "agents.nls"
  "environment.nls"
]

to setup
  clear-all
  setup-environment
  setup-agents
  reset-ticks
end

to go
  move-agents
  tick
end
