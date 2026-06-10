from app.repositories.user_repository import UserRepository


class UserStatusService:
    def __init__(
        self,
        user_repository: UserRepository
    ):
        self.user_repository = user_repository

    async def mark_online(
        self,
        user_id: int
    ):
        return await self.user_repository.update_online_status(
            user_id=user_id,
            is_online=True
        )

    async def mark_offline(
        self,
        user_id: int
    ):
        return await self.user_repository.update_online_status(
            user_id=user_id,
            is_online=False
        )