""" Određivanje vrste kontaktnih sočiva

    Sistemi za podršku odlučivanju:
    Primer realizacije ekspertnog sistema u jeziku Python (Python 3)
    -- na osnovu https://github.com/jhenahan/pycin (Python 2)

"""

# Pomoćne funkcije

def eq(x, y):
    if x == 'nisam siguran':
        return False
    return x == y


# DEFINISANJE SISTEMA

# Kontekst odlučivanja

def define_ctxs(sh):
    #sh.define_ctx(Ctx('pacijent', ['kako oko suzi', 'astigmatizam','vrsta dioptrije']))
    sh.define_ctx(Ctx('pacijent', goals=['preporuka']))


# Parametri (atributi)

def define_params(sh):
    
    # Parametri pacijenta
    sh.define_param(Param('kako oko suzi', 'pacijent', enum=['normalno', 'smanjeno'], ask_first=True))
    sh.define_param(Param('astigmatizam', 'pacijent', enum=['da', 'ne'], ask_first=True))
    sh.define_param(Param('vrsta dioptrije', 'pacijent', enum=['kratkovidost', 'dalekovidost'], ask_first=True))

    # Parametri klasa (odluka) - preporuke sočiva
    sh.define_param(Param('preporuka', 'pacijent', enum=['meka sočiva', 'tvrda sočiva', 'ne preporučuju se']))


# Produkciona pravila

def define_rules(sh):
    # Pravila
    sh.define_rule(Rule(1,
                        [('kako oko suzi', 'pacijent', eq, 'smanjeno')],
                        [('preporuka', 'pacijent', eq, 'ne preporučuju se')],
			1.0))
    sh.define_rule(Rule(2,
                        [('astigmatizam', 'pacijent', eq, 'ne')],
                        [('preporuka', 'pacijent', eq, 'meka sočiva')],
			0.86))
    sh.define_rule(Rule(3,
                        [('vrsta dioptrije', 'pacijent', eq, 'kratkovidost')],
                        [('preporuka', 'pacijent', eq, 'tvrda sočiva')],
			1.0))
    # Default pravilo
    sh.define_rule(Rule(4,
                        [],
                        [('preporuka', 'pacijent', eq, 'ne preporučuju se')],
			0.75))
    
# POKRETANJE SISTEMA

from expert_shell import Param, Ctx, Rule, Shell

def report_findings(findings):
    for inst, result in findings.items():
        print('\nOdluka za %s-%d:' % (inst[0], inst[1]))
        for param, vals in result.items():
            possibilities = ['%s %f' % (val[0], val[1]) for val in vals.items()]
            print('%s: %s' % (param, ', '.join(possibilities)))
        
def main():
    sh = Shell()
    define_ctxs(sh)
    define_params(sh)
    define_rules(sh)
    report_findings(sh.execute(['pacijent']))

main()