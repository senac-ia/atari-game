import gymnasium

# https://pypi.org/project/colorama/
from colorama import just_fix_windows_console, init, Back

init(autoreset=True)

# use Colorama to make Termcolor work on Windows too
just_fix_windows_console()

env = gymnasium.make("ALE/Tennis-v5", render_mode="human", obs_type="ram")
observation, info = env.reset(seed=42)
#for _ in range(1000):
while True:
  # definição da política
  acao = env.action_space.sample()

  ambiente, recompensa, finalizado, paralizado, info = env.step(acao)
  recompensa_txt = "Recompensa: [%s]" % recompensa
  fim_txt = "Finalizado: [%s]" % finalizado
  acao_txt = "Ação: [%s]" % acao

  if (recompensa < 0):
    recompensa_txt = Back.RED + recompensa_txt + Back.RESET
  elif (recompensa > 0):
    recompensa_txt = Back.GREEN + recompensa_txt + Back.RESET

  if (finalizado):
    fim_txt = Back.RED + fim_txt + Back.RESET

  print(recompensa_txt, fim_txt, acao_txt)

  if finalizado or paralizado:
    break
    #ambiente, info = env.reset()
env.close()