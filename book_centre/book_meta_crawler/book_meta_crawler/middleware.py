import random
from user_agents import USER_AGENTS


class UserAgentMiddleware(object):
    def process_request(self, request, spider):
        agent = random.choice(USER_AGENTS)
        request.headers["User-Agent"] = agent
