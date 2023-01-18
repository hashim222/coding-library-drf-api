from rest_framework import generics, permissions
from coding_library.permissions import IsOwnerOrReadOnly
from .models import ContactForm
from .serializers import ContactFormSerializer


class ContactList(generics.ListCreateAPIView):
    """
    List contacts or create a contact if logged in.
    """
    serializer_class = ContactFormSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = ContactForm.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a contact, or update or delete it by id.
    """
    serializer_class = ContactFormSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = ContactForm.objects.all()
