from mamba import description, context, it, before, after, after_all, before_all
from expects import expect, equal

with description('Use Case') as self:
    with before.all:
        print('Antes de TODOS test (Before each)')
    with after.all:
        print('Después de TODOS test (Before each)')
    with before.each:
        print('Antes de vecada test (Before each)')
    with after.each:
        print('Después de cada test (Before each)')


    with context('Use contest'):
        with it('Able to do something 1'):
            print('test 1')
            expect(True).to(equal(True))

        with it('Able to do something 2'):
            print('test 2')
            expect(True).to(equal(True))
