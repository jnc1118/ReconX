from rich.console import Console
from rich.table import Table

console = Console()


def show_target_info(target_info):
    """
    Display target information in a professional table.
    """

    table = Table(title="\nTarget Information")

    table.add_column("Field", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")

    table.add_row("Original Input", target_info["original"])
    table.add_row("Hostname", target_info["hostname"])
    table.add_row("IP Address", target_info["ip"])
    table.add_row("Scheme", target_info["scheme"])

    console.print(table)


def show_dns_records(dns_records):
    """
    Display DNS records in a professional table.
    """

    table = Table(title="\nDNS Records")

    table.add_column("Record Type", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")

    for record_type, values in dns_records.items():

        if values:
            for value in values:
                table.add_row(record_type, value)
        else:
            table.add_row(record_type, "[red]No records found[/red]")

    console.print(table)

def show_whois_info(whois_info):
    """
    Display WHOIS information in a Rich table.
    """

    table = Table(title="\nWHOIS Information")

    table.add_column("Field", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")

    for key, value in whois_info.items():

        if isinstance(value, list):
            value = "\n".join(str(v) for v in value)

        table.add_row(str(key), str(value))

    console.print(table)