from rest_framework import permissions


class IsOwnerOnly(permissions.BasePermission):
	"""
	Permiso personalizado solo los usuario propietarios del objeto pueden
	realizar acciones con el.
	"""
	def has_object_permission(self, request, view, obj):
		return obj.user == request.user