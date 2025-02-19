# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import inlineformset_factory

from SGEO.apps.financeiro.models import PlanoContasGrupo, PlanoContasSubgrupo, CentroCusto


class PlanoContasGrupoForm(forms.ModelForm):

    class Meta:
        model = PlanoContasGrupo
        fields = ('tipo_grupo', 'descricao',)
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_grupo': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'descricao': _('Descrição'),
            'tipo_grupo': _('Tipo de lançamento'),
        }


class CentroCustoForm(forms.ModelForm):

    class Meta:
        model = CentroCusto
        fields = ('descricao',)
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'descricao': _('Descrição'),
        }



class PlanoContasSubgrupoForm(forms.ModelForm):

    class Meta:
        model = PlanoContasSubgrupo
        fields = ('descricao',)
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'descricao': _('Descrição'),
        }


PlanoContasSubgrupoFormSet = inlineformset_factory(
    PlanoContasGrupo, PlanoContasSubgrupo, form=PlanoContasSubgrupoForm, fk_name='grupo', extra=1, can_delete=True)
