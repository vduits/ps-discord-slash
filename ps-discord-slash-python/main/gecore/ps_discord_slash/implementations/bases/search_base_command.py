from gecore.ps_discord_slash.commands.command_interface import ISlashCommand
from gecore.ps_discord_slash.implementations.available_commands import OvOSlashCommand
from gecore.ps_discord_slash.implementations.bases.models.base_response import create_base_response
from gecore.ps_discord_slash.implementations.bases.search_bases import find_bases
from gecore.ps_discord_slash.models.commands import ApplicationCommand, ApplicationCommandOption, \
    ApplicationCommandOptionType
from gecore.ps_discord_slash.models.discord_config import GenericConfig
from gecore.ps_discord_slash.models.interactions import InteractionResponse


class SearchBaseSlashCommand(ISlashCommand):

    @staticmethod
    def identify() -> OvOSlashCommand:
        return OvOSlashCommand.SEARCH_BASE_ID

    @staticmethod
    def build(command_id: int, guild_id: int, version: int) -> ApplicationCommand:
        return ApplicationCommand(
            command_id=str(command_id),
            app_id=str(GenericConfig.APP_ID),
            name=OvOSlashCommand.SEARCH_BASE_ID,
            description='Search a facility Id [v2]',
            version=version,
            guild_id=guild_id,
            options=[ApplicationCommandOption(
                a_type=ApplicationCommandOptionType.STRING,
                name='ByName',
                description='Put in a name to return matching bases and their ids',
                required=True
            )]
        )

    @staticmethod
    def execute(command_body: {}) -> InteractionResponse:
        search_arg = command_body['data']['options'][0]['value']
        base_result = find_bases(search_arg)
        return create_base_response(base_result, search_arg)