from djongo import models

class Host(models.Model):
    host           = models.CharField(max_length=200)
    vendor         = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return '(%s) - %s  (%s)' % (self.id, self.host, self.vendor)

class Backup(models.Model):
    host_id     = models.ForeignKey(Host,related_name='backups',on_delete=models.CASCADE)
    state       = models.CharField(blank=True,max_length=20)
    start_time  = models.DateTimeField()
    finish_time = models.DateTimeField(blank=True)
    duration    = models.CharField(max_length=100, blank=True)
    filename    = models.CharField(max_length=200)
    location    = models.CharField(max_length=200)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '(%s) - %s  ( %s )' % (self.id, self.host_id.host, self.start_time)
