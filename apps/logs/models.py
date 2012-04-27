from django.db import models


class Entry(models.Model):
    dtime = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=5)
    path = models.CharField(max_length=255)
    meta = models.TextField()

    def __unicode__(self):
        return '[%s] "%s %s"' % (self.dtime.strftime('%d.%m.%Y %H:%M:%S'),
                self.method, self.path)
