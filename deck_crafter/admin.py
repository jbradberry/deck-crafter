from django.contrib import admin

from .models import Game, Edition, Card


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Edition)
class EditionAdmin(admin.ModelAdmin):
    list_display = ('name', 'game_name')
    list_select_related = ('game',)

    def game_name(self, obj):
        return obj.game.name


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'edition_name', 'game_name')
    list_select_related = ('edition__game',)

    def game_name(self, obj):
        return obj.edition.game.name

    def edition_name(self, obj):
        return obj.edition.name
