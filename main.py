import gymnasium

# https://pypi.org/project/colorama/
from colorama import just_fix_windows_console, init, Back, Fore

init(autoreset=True)

# use Colorama to make Termcolor work on Windows too
just_fix_windows_console()

env = gymnasium.make("ALE/Tennis-v5", render_mode="human", obs_type="ram")
ambiente, info = env.reset(seed=42)

def convert(n):
  out = 0
  # https://realpython.com/python-bitwise-operators/
  for bit in n:
    out = (out << 1) | bit
  return out

ambiente_txt = "Ambiente [%s]" % convert(ambiente)
print(ambiente_txt, "Tamanho: " + str(len(ambiente)))

while True:
  # definição da política
  acao = env.action_space.sample()

  ambiente, recompensa, finalizado, paralizado, info = env.step(acao)
  ambiente_txt = "Ambiente [%s]" % convert(ambiente)
  recompensa_txt = "Recompensa: [%s]" % recompensa
  fim_txt = "Finalizado: [%s]" % finalizado
  acao_txt = "Ação: [%s]" % acao

  if (recompensa < 0):
    recompensa_txt = Fore.RED + recompensa_txt + Fore.RESET
  elif (recompensa >= 0):
    recompensa_txt = Fore.GREEN + recompensa_txt + Fore.RESET

  if (finalizado):
    fim_txt = Fore.RED + fim_txt + Fore.RESET

  print(ambiente_txt, recompensa_txt, fim_txt, acao_txt)

  if finalizado or paralizado:
    break
    #ambiente, info = env.reset()
env.close()