"""Compatibilidade: ensaio de Convenios retirado; nao permite reativacao."""
import argparse
import integrar_convenios

def set_mode(root=integrar_convenios.ROOT, active=True):
    if active:
        raise ValueError('Ensaio retirado. Use tools/integrar_convenios.py para os dados reais.')
    if root != integrar_convenios.ROOT:
        raise ValueError('Use o importador real explicitamente no projeto correto.')
    integrar_convenios.run()

if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    g=p.add_mutually_exclusive_group(required=True)
    g.add_argument('--ativar',action='store_true');g.add_argument('--desativar',action='store_true');g.add_argument('--check',action='store_true')
    args=p.parse_args()
    if args.ativar:p.error('Ensaio retirado; reativacao bloqueada. Use integrar_convenios.py.')
    integrar_convenios.run(check=args.check)
