from .models import Host, Backup
from rest_framework import serializers

class BackupSerializer(serializers.HyperlinkedModelSerializer):
    # host = HostSerializer(read_only=True, many=True)

    # host_id = HostSerializer()
    class Meta:
        model = Backup
        fields = ('state', 'start_time', 'finish_time', 'filename', 'location')

    # def create(self, validated_data):
    #     host_id = validated_data.pop('host_id')
    #     h = Host.objects.create(**host_id)
    #     backup = Backup.objects.create(host_id=h, **validated_data)
    #     return backup

class HostSerializer(serializers.HyperlinkedModelSerializer):
    # backups = serializers.PrimaryKeyRelatedField(queryset=Backup.objects.all(), many=True)
    backups  = BackupSerializer(many=True)
    class Meta:
        model = Host
        fields = ('id', 'host', 'vendor', 'backups')
