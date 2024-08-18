import faiss


def save_vector_store_for_user(db, user, vector_store):
    # Serialize the FAISS index
    index_binary = faiss.serialize_index(vector_store)

    # Store it in the user's vector_store field
    user.vector_store = index_binary

    # Commit the changes to the database
    db.session.commit()


def get_vector_store_for_user(user):
    if user.vector_store:
        # Deserialize the FAISS index
        vector_store = faiss.deserialize_index(user.vector_store)
        return vector_store
    else:
        return None  # No vector store available for this user
