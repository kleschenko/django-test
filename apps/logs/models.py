from django.db import models


class Entry(models.Model):
    dtime = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=5)
    path = models.CharField(max_length=255)
    meta = models.TextField()

    @models.permalink
    def get_absolute_url(self):
        return ('logs_view', [self.id])

    def __unicode__(self):
        return '[%s] "%s %s"' % (self.dtime.strftime('%d.%m.%Y %H:%M:%S'),
                self.method, self.path)

    class Meta:
        verbose_name_plural = "entries"
