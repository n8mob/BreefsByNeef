from django.db import models


class Breef(models.Model):
    text = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        if self.title:
            return self.title
        elif self.text:
            return self.text.split('\n')[0]
        else:
            return 'empty breef'


class Section(models.Model):
    slug = models.SlugField()

    def __str__(self):
        return self.slug


class Page(models.Model):
    number = models.PositiveSmallIntegerField(null=False)  # not unique!
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)

    def __str__(self):
        if str(self.section).casefold() == 'frontmatter'.casefold():
            return roman_numeral(self.number)
        else:
            return str(self.number)


class PageBreef(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    breef = models.ForeignKey(Breef, on_delete=models.CASCADE)
    sort_order = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.breef) + ' on page ' + str(self.page)

    class Meta:
        ordering = ['page', 'sort_order']


def roman_numeral(n):
    """ only calculates 'simplistic' roman numerals,
    that is, no prefixes: 4 => iiii instead of iv

    Args:
        n: the number to convert <em>into</em> roman numerals

    Returns: the value of n as a (simplistic) roman numeral

    """
    if n > 3999:
        return str(n)

    r = ''

    while n >= 1000:
        r += 'm'
        n -= 1000

    while n >= 500:
        r += 'd'
        n -= 500

    while n >= 100:
        r += 'c'
        n -= 100

    while n >= 50:
        r += 'l'
        n -= 50

    while n >= 10:
        r += 'x'
        n -= 10

    while n >= 5:
        r += 'v'
        n -= 5

    while n >= 1:
        r += 'i'
        n -= 1

    return r
