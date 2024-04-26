from typing import AsyncIterator, Any

from nestipy.graphql import Resolver, Query, Mutation, Subscription
from nestipy_ioc import Inject, Args

from .user_input import UserInput
from .user_service import UserService
from ..pubsub import PubSub


@Resolver()
class UserResolver:
    user_service: Inject[UserService]
    pub_sub: Inject[PubSub]

    @Query()
    async def user_test_query(self) -> str:
        self.pub_sub.publish('message', 'from query')
        return await self.user_service.list()

    @Mutation()
    async def user_test_mutation(self, data: Args[UserInput]) -> str:
        self.pub_sub.publish('message', 'from mutation')
        return data.test

    @Subscription()
    async def test_subscription(self) -> AsyncIterator[str]:
        return self.pub_sub.asyncIterator('message')
